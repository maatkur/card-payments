import os

import openpyxl
from openpyxl.styles import Font

from database.db_handler import DatabaseHandler
from helpers import to_default_format, to_date_string


def generate_conference_report(initial_date, final_date, cashier_number):
    handler = DatabaseHandler()  # Instancia o banco de dados

    handler.connect()  # conecta com o banco de dados

    orders = handler.get_orders_to_conference_report(initial_date, final_date, cashier_number)

    workbook = openpyxl.Workbook()  # Crie um arquivo temporário
    worksheet = workbook.active  # Seleciona a folha de trabalho do excel

    header = ["Pedido", "Caixa", "Movimento", "Transação", "Bandeira", "Parcelas", "Valor da parcela", "Valor do pedido",
              "Data da venda"]  # Cria o cabeçalho

    # Adiciona informações à planilha
    worksheet.append(header)
    for order in orders:
        order_number = order[0]
        cashier = order[1]
        cash_flow = order[2]
        transaction_type = "Débito" if order[3] == "debit" else "Crédito"
        flag = order[4]
        installments = order[5]
        installment_value = order[6]
        order_value = order[7]
        purchase_date = to_default_format(order[8])

        worksheet.append(
            [order_number, cashier, cash_flow, transaction_type, flag, installments, installment_value, order_value,
             purchase_date])

    # Definir o estilo do cabeçalho em negrito
    bold_font = Font(bold=True)
    for cell in worksheet[1]:
        cell.font = bold_font

    # Salva o arquivo temporário
    user = os.getlogin()
    date = to_date_string()
    temp_filename = rf'C:\Users\{user}\Desktop\cartoes{date}.xlsx'
    workbook.save(temp_filename)

    # Abra o arquivo temporário no Excel
    os.system(f'start excel.exe "{temp_filename}"')


if __name__ == "__main__":
    generate_conference_report("", "")