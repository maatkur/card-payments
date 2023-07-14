import pandas as pd
from helpers.date_helpers import DateHelpers

from dotenv import load_dotenv

from helpers.string_helpers import StringHelpers

load_dotenv("./development.env")

cielo_file = pd.read_excel(r"C:\Users\Matheus\PycharmProjects\trykat-card\tmp\recebimento.xlsx")


def teste_cielo():
    cielo_payments = []

    for index, row in cielo_file.iterrows():

        cielo_transaction_type = str(row["Forma de Pagamento"])
        cielo_payday = row["Data de pagamento"]

        if "Débito" in cielo_transaction_type:
            continue

        if cielo_payday != '11/07/2023':
            continue

        cielo_payment = {
            "transactionType": cielo_transaction_type,
            "flag": row["Bandeira"],
            "payday": DateHelpers.to_sql_format(cielo_payday),
            "flagTax": row["Taxas (%)"].replace(",", "."),
            "purchaseDate": DateHelpers.to_sql_format(row["Data da autorização da venda"]),
            "installments": "1" if "Crédito à vista" in cielo_transaction_type else str(row["Quantidade de parcelas"]),
            "currentInstallment": "1" if "Crédito à vista" in cielo_transaction_type else str(row["Número da parcela"]),
            "installmentValue": float(StringHelpers.clear_excel_caracters(row["Valor líquido"])),
            "NSU": str(row["NSU"]),
            "transactionAuthorization": str(row["Código de autorização"]),
            "oldCurrentInstallment": str(row["Número da parcela"]),
            "oldInstallments": str(row["Quantidade de parcelas"])
        }

        cielo_payments.append(cielo_payment)

    return cielo_payments
