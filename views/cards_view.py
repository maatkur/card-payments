import os
import sys
from datetime import datetime

from PySide6 import QtCore
from PySide6.QtCore import QDate
from PySide6.QtWidgets import *

from views.cards_details_view import CardDetails
from database.repositories.order_stage_repository import OrderStageRepository
from database.repositories.checked_orders_repository import CheckedOrdersRepository
from reports.conference_report import generate_conference_report
from helpers.date_helpers import to_sql_format
from views.manual_insert_view import AddPayment
from ui.ui_cards import Ui_MainWindow
from views.card_management_view import CardsManagement
from components.dialog_window import DialogWindow


class Cards(QMainWindow):
    today = datetime.today()
    qdate = QDate(today.year, today.month, today.day)

    def __init__(self, user_type, store, user_code) -> None:
        super(Cards, self).__init__()
        self.ui = Ui_MainWindow()  # instanciar a classe Ui_MainWindow
        self.ui.setupUi(self)
        self.setWindowTitle(f"Cartões {os.getenv('COMPANY')} | Lançamento")
        self.user_type = user_type
        self.store = store
        self.user_code = user_code
        self.order_stage_repository = OrderStageRepository()
        self.checked_orders_repository = CheckedOrdersRepository()
        self.manage_orders_table()
        self.disable_search_button()
        self.manage_user_permission()
        self.details_window = None
        self.add_payment_window = None
        self.cards_management_window = None
        self.dialog_window = DialogWindow()
        self.ui.tableWidget.setColumnWidth(2, 88)  # Definindo a largura da coluna da data para 88 pixels
        self.connect_button_actions()
        self.connect_text_changes()
        self.ui.initial_date.setDate(self.qdate)
        self.ui.final_date.setDate(self.qdate)
        self.ui.search_order_entry.installEventFilter(self)
        self.ui.search_button.installEventFilter(self)

    def eventFilter(self, widget, event) -> bool:
        if event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            if key == QtCore.Qt.Key_Return or key == QtCore.Qt.Key_Enter:
                if widget == self.ui.search_order_entry:
                    self.handle_search_button()
                if widget == self.ui.search_button:
                    self.handle_search_button()

        return False

    def connect_button_actions(self) -> None:
        self.ui.tableWidget.cellDoubleClicked.connect(
            self.handle_cell_double_click)  # Conectando o evento de duplo clique a um slot
        self.ui.add_card_payment_button.clicked.connect(self.handle_add_payment_button)
        self.ui.search_button.clicked.connect(self.handle_search_button)
        self.ui.excel_report_button.clicked.connect(self.handle_report_button)
        self.ui.refresh_button.clicked.connect(self.handle_refresh_button)
        self.ui.management_button.clicked.connect(self.handle_management_button)

    def connect_text_changes(self) -> None:
        self.ui.search_order_entry.textChanged.connect(self.manage_search_button)

    def load_orders_table(self, data: list):

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

    def manage_user_permission(self) -> None:
        is_admin_user = self.user_type == "True"

        if is_admin_user:
            self.enable_admin_buttons()
        else:
            self.disable_admin_button()

    def get_orders_data(self) -> list:
        is_admin_user = self.user_type == "True"

        if is_admin_user:
            data = self.order_stage_repository.get_uncommited_orders(self.store)
        else:
            data = self.order_stage_repository.get_uncommited_orders(self.store, self.user_code)

        return data

    def manage_orders_table(self) -> None:
        data = self.get_orders_data()
        self.load_orders_table(data)

    def get_filtered_order(self, order_number) -> list:
        is_admin_user = self.user_type == "True"

        if is_admin_user:
            data = self.order_stage_repository.filter_uncommited_order(self.store, order_number)
        else:
            data = self.order_stage_repository.filter_uncommited_order(self.store, order_number, self.user_code)

        return data

    def load_filtered_order(self) -> None:
        order_number = self.ui.search_order_entry.text()
        data = self.get_filtered_order(order_number)
        not_found = len(data) == 0

        if not_found:
            self.dialog_window.not_found()
        else:
            self.load_orders_table(data)

    def handle_cell_double_click(self, row, column) -> None:

        order = self.ui.tableWidget.item(row, 0).text()  # pega o valor da coluna "Pedido"
        self.details_window = CardDetails(order, self.user_type, self.store)
        self.details_window.show()
        self.details_window.closed.connect(self.manage_orders_table)

    def handle_add_payment_button(self) -> None:
        self.add_payment_window = AddPayment()
        self.add_payment_window.clear_fields()
        self.add_payment_window.show()
        self.add_payment_window.closed.connect(self.manage_orders_table)

    def handle_report_button(self) -> None:
        initial_date = to_sql_format(self.ui.initial_date.text())
        final_date = to_sql_format(self.ui.final_date.text())

        checked_orders_repository = CheckedOrdersRepository()

        options = {
            "select": "orderNumber, cashierNumber, cashFlow, transactionType, flag, installments, installmentValue, "
                      "orderValue, purchaseDate, NSU, transactionAuthorization",
            "distinct": True,
            "query": {
                "cashierNumber": self.user_code,
                "initial_date": initial_date,
                "final_date": final_date
            },
            "order_by": ["flag"]
        }

        orders = checked_orders_repository.get_all(options)
        generate_conference_report(orders)

    def handle_management_button(self) -> None:
        self.cards_management_window = CardsManagement()
        self.cards_management_window.show()

    def handle_search_button(self) -> None:
        self.load_filtered_order()
        self.clear_fields()

    def handle_refresh_button(self) -> None:
        self.manage_orders_table()

    def disable_search_button(self) -> None:
        self.ui.search_button.setDisabled(True)

    def enable_search_button(self) -> None:
        self.ui.search_button.setDisabled(False)

    def disable_admin_button(self) -> None:
        self.ui.add_card_payment_button.setDisabled(True)
        self.ui.management_button.setDisabled(True)

    def enable_admin_buttons(self) -> None:
        self.ui.add_card_payment_button.setDisabled(False)
        self.ui.management_button.setDisabled(False)

    def manage_search_button(self) -> None:
        is_order_entry_filled = len(self.ui.search_order_entry.text()) >= 5

        if is_order_entry_filled:
            self.enable_search_button()
        else:
            self.disable_search_button()

    def clear_fields(self) -> None:
        self.ui.search_order_entry.setText('')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cards("True", 7, 15)
    window.show()
    app.exec()


