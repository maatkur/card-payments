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
                "status": row["Status"],
                "oldCurrentInstallment": str(row["Número da parcela"]),
                "oldInstallments": str(row["Quantidade de parcelas"])
            }

            payments.append(carrier_payment)

        self.carrier_payments = payments

    def find_payments(self):

        found_payments = []
        old_found_payments = []
        not_found_payments = []

        for payment in self.carrier_payments:
            payment_was_found = False

            payment_search = RepositoryManager.checked_orders_repository().get_unconciliated_order({
                "NSU": payment["NSU"],
                "transactionAuthorization": payment["transactionAuthorization"],
                "currentInstallment": f'{payment["currentInstallment"]}/{payment["installments"]}',
            })

            old_payments_search = RepositoryManager.old_payments_repository().get_unconciliated_order({
                "NSU": payment["NSU"],
                "transactionAuthorization": payment["transactionAuthorization"],
                "currentInstallment": payment["oldCurrentInstallment"]
            })

            if payment_search:
                if payment_search["conciliated"]:
                    continue
                else:
                    payment_search["payday"] = payment["payday"]
                    payment_search["status"] = payment["status"]
                    found_payments.append(payment_search)
                    payment_was_found = True

            if old_payments_search:
                if old_payments_search["conciliated"]:
                    continue
                else:
                    old_payments_search["payday"] = payment["payday"]
                    old_payments_search["status"] = payment["status"]
                    old_found_payments.append(old_payments_search)
                    payment_was_found = True

            if not payment_was_found:
                not_found_payments.append(payment)

        found_payments = sorted(found_payments, key=lambda x: x['orderNumber'])

        return old_found_payments, found_payments, not_found_payments

    def find_payments_status(self):
        uid_and_status = []
        old_uid_and_status = []

        for payment in self.carrier_payments:
            # Realiza a busca no repositório atual
            payment_search = RepositoryManager.checked_orders_repository().get_unconciliated_order({
                "NSU": payment["NSU"],
                "transactionAuthorization": payment["transactionAuthorization"],
                "currentInstallment": f'{payment["currentInstallment"]}/{payment["installments"]}',
                "conciliated": "1"
            })

            if payment_search:
                uid_and_status.append({
                    "uId": payment_search["uId"],
                    "currentInstallment": payment_search["currentInstallment"],
                    "status": payment["status"]
                })
            else:
                # Se o pagamento não foi encontrado, realiza a busca no repositório antigo
                old_payment_search = RepositoryManager.old_payments_repository().get_unconciliated_order({
                    "NSU": payment["NSU"],
                    "transactionAuthorization": payment["transactionAuthorization"],
                    "currentInstallment": payment["oldCurrentInstallment"],
                    "conciliated": "1"
                })

                if old_payment_search:
                    old_uid_and_status.append({
                        "uId": old_payment_search["uId"],
                        "currentInstallment": old_payment_search["currentInstallment"],
                        "status": payment["status"]
                    })

        return uid_and_status, old_uid_and_status


if __name__ == "__main__":
    carrier_excel = CarrierExcel()
