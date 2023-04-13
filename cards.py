import sys
from datetime import datetime

from PySide6 import QtCore
from PySide6.QtCore import QDate
from PySide6.QtWidgets import *

from cards_details import CardDetails
from database.db_handler import DatabaseHandler
from excel_reports import generate_conference_report
from helpers import to_sql_format
from manual_insert import AddPayment
from ui.ui_cards import Ui_MainWindow


class CardView(QMainWindow):
    today = datetime.today()
    qdate = QDate(today.year, today.month, today.day)

    def __init__(self, user_type, store, user_code) -> None:
        super(CardView, self).__init__()
        self.ui = Ui_MainWindow()  # instanciar a classe Ui_MainWindow
        self.ui.setupUi(self)
        self.setWindowTitle("Cartões Obra Fácil | Lançamento")
        self.user_type = user_type
        self.store = store
        self.user_code = user_code
        self.manage_orders_table()
        self.ui.search_button.setDisabled(True)
        self.manage_payment_button_use()
        self.details_window = None
        self.add_payment_window = None
        self.ui.tableWidget.setColumnWidth(2, 88)  # Definindo a largura da coluna da data para 154 pixels
        self.ui.tableWidget.cellDoubleClicked.connect(
            self.handle_cell_double_click)  # Conectando o evento de duplo clique a um slot
        self.ui.add_card_payment_button.clicked.connect(self.handle_add_payment_button)
        self.ui.search_button.clicked.connect(self.handle_search_button)
        self.ui.initial_date.setDate(self.qdate)
        self.ui.final_date.setDate(self.qdate)
        self.ui.excel_report_button.clicked.connect(self.handle_report_button)
        self.ui.search_order_entry.textChanged.connect(self.verify_order_entry)
        self.ui.refresh_button.clicked.connect(self.handle_refresh_button)
        self.ui.search_order_entry.installEventFilter(self)
        self.ui.search_button.installEventFilter(self)

    def eventFilter(self, widget, event) -> None:
        if event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            if key == QtCore.Qt.Key_Return or key == QtCore.Qt.Key_Enter:
                if widget == self.ui.search_order_entry:
                    self.handle_search_button()
                if widget == self.ui.search_button:
                    self.handle_search_button()

    def show_payments(self, data: list):
        # db_handler.get_orders_by_store_and_cashier(self.store, self.user_code)

        orders = data
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

    def manage_payment_button_use(self):
        is_admin_user = self.user_type == "True"

        if is_admin_user:
            self.enable_insert_payment_button()
        else:
            self.disable_insert_payment_button()

    def get_table_data(self):
        is_admin_user = self.user_type == "True"

        db_handler = DatabaseHandler()
        db_handler.connect()

        if is_admin_user:
            data = db_handler.get_all_orders_by_store(self.store)
        else:
            data = db_handler.get_orders_by_store_and_cashier(self.store, self.user_code)

        db_handler.disconnect()

        return data

    def manage_orders_table(self):
        data = self.get_table_data()
        self.show_payments(data)

    def get_search_data(self, order_number):
        is_admin_user = self.user_type == "True"

        db_handler = DatabaseHandler()
        db_handler.connect()

        if is_admin_user:
            data = db_handler.get_specific_order_by_store(self.store, order_number)
        else:
            data = db_handler.get_order_by_cashier_filter(self.store, self.user_code)

        db_handler.disconnect()

        return data

    def manage_search_button(self):
        order_number = self.ui.search_order_entry.text()
        data = self.get_search_data(order_number)
        self.show_payments(data)

    def handle_cell_double_click(self, row, column):
        if self.details_window is not None:
            order = self.ui.tableWidget.item(row, 0).text()  # pega o valor da coluna "Pedido"
            self.details_window.clear_fields()
            self.details_window.update_data(order)
            self.details_window.show()
            return

        order = self.ui.tableWidget.item(row, 0).text()  # pega o valor da coluna "Pedido"
        self.details_window = CardDetails(order, self.user_type, self.store)
        self.details_window.show()
        self.details_window.closed.connect(self.show_payments)

    def handle_add_payment_button(self):
        if self.add_payment_window is not None:
            self.add_payment_window.show()
            self.add_payment_window.clear_fields()
            return

        self.add_payment_window = AddPayment(self.store)
        self.add_payment_window.clear_fields()
        self.add_payment_window.show()
        self.add_payment_window.closed.connect(self.show_payments)

    def handle_report_button(self):
        initial_date = to_sql_format(self.ui.initial_date.text())
        final_date = to_sql_format(self.ui.final_date.text())

        generate_conference_report(initial_date, final_date, self.user_code)

    def handle_search_button(self):
        self.manage_search_button()
        self.clear_fields()

    def handle_refresh_button(self):
        self.manage_orders_table()

    def disable_search_button(self):
        self.ui.search_button.setDisabled(True)

    def enable_search_button(self):
        self.ui.search_button.setDisabled(False)

    def verify_order_entry(self):
        is_order_entry_filled = len(self.ui.search_order_entry.text()) == 6

        if is_order_entry_filled:
            self.enable_search_button()
        else:
            self.disable_search_button()

    def disable_insert_payment_button(self):
        self.ui.add_card_payment_button.setDisabled(True)

    def enable_insert_payment_button(self):
        self.ui.add_card_payment_button.setDisabled(False)

    def clear_fields(self):
        self.ui.search_order_entry.setText('')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CardView("True", 1, 83)
    window.show()
    app.exec()


