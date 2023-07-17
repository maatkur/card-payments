import pandas as pd
from helpers.date_helpers import DateHelpers

from dotenv import load_dotenv

from helpers.string_helpers import StringHelpers

from database.repositories.repository_manager import RepositoryManager

load_dotenv("./development.env")


class CarrierExcel:
    def __init__(self, file_path):
        self.carrier_file = pd.read_excel(file_path)
        self.carrier_payments = None

    def load_carrier_payments(self, date_period: dict) -> None:

        initial_date = DateHelpers.to_date_obj(date_period.get("initial_date"))
        final_date = DateHelpers.to_date_obj(date_period.get("final_date"))

        payments = []

        for index, row in self.carrier_file.iterrows():

            carrier_transaction_type = str(row["Forma de Pagamento"])
            carrier_payday = (row["Data de pagamento"])

            if DateHelpers.to_date_obj(carrier_payday) < initial_date or DateHelpers.to_date_obj(
                    carrier_payday) > final_date:
                continue

            carrier_payment = {
                "transactionType": carrier_transaction_type,
                "flag": row["Bandeira"],
                "payday": DateHelpers.to_sql_format(carrier_payday),
                "flagTax": row["Taxas (%)"].replace(",", "."),
                "purchaseDate": DateHelpers.to_sql_format(row["Data da autorização da venda"]),
                "installments": "1" if "Crédito à vista" in carrier_transaction_type else str(
                    row["Quantidade de parcelas"]),
                "currentInstallment": "1" if "Crédito à vista" in carrier_transaction_type else str(
                    row["Número da parcela"]),
                "installmentValue": float(StringHelpers.clear_excel_caracters(row["Valor líquido"])),
                "NSU": str(row["NSU"]),
                "transactionAuthorization": str(row["Código de autorização"]),
                "oldCurrentInstallment": str(row["Número da parcela"]),
                "oldInstallments": str(row["Quantidade de parcelas"])
            }

            payments.append(carrier_payment)

        self.carrier_payments = payments

    def match_payments(self):

        found_payments = []
        old_found_payments = []
        not_found_payments = []

        for payment in self.carrier_payments:
            payment_was_found = False

            payment_search = RepositoryManager.checked_orders_repository().get_conciliations({
                "NSU": payment["NSU"],
                "transactionAuthorization": payment["transactionAuthorization"],
                "currentInstallment": f'{payment["currentInstallment"]}/{payment["installments"]}',
            })

            old_payments_search = RepositoryManager.old_payments_repository().get_conciliations({
                "NSU": payment["NSU"],
                "transactionAuthorization": payment["transactionAuthorization"],
                "currentInstallment": payment["oldCurrentInstallment"]
            })

            if payment_search:
                if payment_search["conciliated"]:
                    continue
                else:
                    payment_search["payday"] = payment["payday"]
                    found_payments.append(payment_search)
                    payment_was_found = True

            if old_payments_search:
                if old_payments_search["conciliated"]:
                    continue
                else:
                    old_payments_search["payday"] = payment["payday"]
                    old_found_payments.append(old_payments_search)
                    payment_was_found = True

            if not payment_was_found:
                not_found_payments.append(payment)

        found_payments = sorted(found_payments, key=lambda x: x['orderNumber'])

        return old_found_payments, found_payments, not_found_payments


if __name__ == "__main__":
    carrier_excel = CarrierExcel()
