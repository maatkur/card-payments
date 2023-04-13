import openpyxl
from openpyxl.styles import Font
import os
from database.db_handler import DatabaseHandler
from helpers import to_default_format


def generate_conference_report(initial_date, final_date, store):

    handler = DatabaseHandler()  # Instancia o banco de dados

    handler.connect()  # conecta com o banco de dados

    orders = handler.get_orders_to_conference(initial_date, final_date, store)

    workbook = openpyxl.Workbook()  # Crie um arquivo temporário
    worksheet = workbook.active  # Seleciona a folha de trabalho do excel

    header = ["Pedido", "Caixa", "Movimento", "Transação", "Bandeira", "Valor", "Data da venda"]  # Cria o cabeçalho

    # Adiciona informações à planilha
    worksheet.append(header)
    for order in orders:
        order_number = order[0]
        cashier = order[1]
        cash_flow = order[2]
        transaction_type = order[3]
        flag = order[4]
        order_value = order[5]
        purchase_date = to_default_format(order[6])

        worksheet.append([order_number, cashier, cash_flow, transaction_type, flag, order_value, purchase_date])

    # Definir o estilo do cabeçalho em negrito
    bold_font = Font(bold=True)
    for cell in worksheet[1]:
        cell.font = bold_font

    # Salva o arquivo temporário
    user = os.getlogin()
    temp_filename = rf'C:\Users\{user}\Desktop\cartoes.xlsx'
    workbook.save(temp_filename)

    # Abra o arquivo temporário no Excel
    os.system(f'start excel.exe "{temp_filename}"')


if __name__ == "__main__":
    generate_conference_report("", "")
