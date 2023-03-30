from datetime import datetime
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import QDate
from ui_cards import Ui_MainWindow
from db_handler import DatabaseHandler
from cards_details_ui import CardDetails
from manual_insert import AddPayment
from excel_reports import generate_conference_report
from helpers import to_sql_format

# TO DO
# ALTERAR O CÓDIGO PARA QUE A LOJA SEJA RECEBIDA COMO PARAMETRO VIA CMD NA CHAMADA DO EXECUTAVEL
# --------------------------O TIPO DE USUÁRIO SEJA RECEBIDO-------------------------------------
# TRAVAR OS BOTÕES DE 'ADICIONAR PAGAMENTO' E 'APAGAR LANÇAMENTO'


class CardView(QMainWindow):

    today = datetime.today()
    qdate = QDate(today.year, today.month, today.day)

    def __init__(self) -> None:
        super(CardView, self).__init__()
        self.ui = Ui_MainWindow()  # instanciar a classe Ui_MainWindow
        self.ui.setupUi(self)
        self.setWindowTitle("Pagamentos com cartão")
        self.show_payments()
        self.details_window = None
        self.add_payment_window = None
        self.ui.tableWidget.setColumnWidth(2, 88)  # Definindo a largura da coluna da data para 154 pixels
        self.ui.tableWidget.cellDoubleClicked.connect(
            self.handle_order_details)  # Conectando o evento de duplo clique a um slot
        self.ui.add_card_payment_button.clicked.connect(self.handle_add_payment_button)
        self.ui.initial_date.setDate(self.qdate)
        self.ui.final_date.setDate(self.qdate)
        self.ui.excel_report_button.clicked.connect(self.handle_report_button)

    def show_payments(self):
        db_handler = DatabaseHandler()
        db_handler.connect()
        orders = db_handler.get_orders_by_store(4)
        self.ui.tableWidget.setRowCount(len(orders))

        for row, order in enumerate(orders):
            for col, value in enumerate(order):
                if col == 1:
                    formatted_value = "{:.2f}".format(round(value, 2))
                    value = formatted_value.replace(".", ",")
                if col == 2:  # verifica se é a coluna da data
                    if isinstance(value, datetime):
                        order_date = value
                    else:
                        order_date = datetime.strptime(value, '%Y-%m-%d')
                    formatted_date = order_date.strftime('%d/%m/%Y')
                    self.ui.tableWidget.setItem(row, col, QTableWidgetItem(formatted_date))
                else:
                    self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(value)))

        db_handler.disconnect()

    def handle_order_details(self, row, column):
        if self.details_window is not None:
            order = self.ui.tableWidget.item(row, 0).text()  # pega o valor da coluna "Pedido"
            self.details_window.update_data(order)
            self.details_window.clear_fields()
            self.details_window.show()
            return

        order = self.ui.tableWidget.item(row, 0).text()  # pega o valor da coluna "Pedido"
        self.details_window = CardDetails(order)
        self.details_window.show()
        self.details_window.closed.connect(self.show_payments)

    def handle_add_payment_button(self):
        if self.add_payment_window is not None:
            self.add_payment_window.show()
            self.add_payment_window.clear_fields()
            return

        self.add_payment_window = AddPayment()
        self.add_payment_window.clear_fields()
        self.add_payment_window.show()
        self.add_payment_window.closed.connect(self.show_payments)

    def handle_report_button(self):
        initial_date = to_sql_format(self.ui.initial_date.text())
        final_date = to_sql_format(self.ui.final_date.text())

        generate_conference_report(initial_date, final_date)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CardView()
    window.show()
    app.exec()
