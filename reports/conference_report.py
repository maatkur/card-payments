import os

import openpyxl
from openpyxl.styles import Font

from database.repositories.checked_orders_repository import CheckedOrdersRepository
from helpers.date_helpers import DateHelpers


def generate_conference_report(data):

    workbook = openpyxl.Workbook()  # Crie um arquivo temporário
    worksheet = workbook.active  # Seleciona a folha de trabalho do excel

    header = ["Pedido", "Caixa", "Movimento", "Transação", "Bandeira", "Valor do pedido", "Parcelas",
              "Valor da parcela",
              "Data da venda", "NSU", "Autorização"]  # Cria o cabeçalho

    # Adiciona informações à planilha
    worksheet.append(header)
    for order in data:
        order_number = order[0]
        cashier = order[1]
        cash_flow = order[2]
        transaction_type = "Débito" if order[3] == "debit" else "Crédito"
        flag = order[4]
        installments = order[5]
        installment_value = order[6]
        order_value = order[7]
        purchase_date = DateHelpers.to_default_format(order[8])
        nsu = order[9]
        transaction_authorization = order[10]

        worksheet.append(
            [order_number, cashier, cash_flow, transaction_type, flag, order_value, installments, installment_value,
             purchase_date, nsu, transaction_authorization])

    # Definir o estilo do cabeçalho em negrito
    bold_font = Font(bold=True)
    for cell in worksheet[1]:
        cell.font = bold_font

    # Salva o arquivo temporário
    user = os.getlogin()
    date = DateHelpers.to_date_string()
    temp_filename = rf'C:\Users\{user}\Desktop\cartoes{date}.xlsx'
    workbook.save(temp_filename)

    # Abra o arquivo temporário no Excel
    os.system(f'start excel.exe "{temp_filename}"')
