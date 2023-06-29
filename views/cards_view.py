import os
import sys
from datetime import datetime

from PySide6 import QtCore
from PySide6.QtCore import QDate
from PySide6.QtWidgets import *

from database.repositories.repository_manager import RepositoryManager
from views.cards_details_view import CardDetails
from reports.conference_report import generate_conference_report
from helpers.date_helpers import DateHelpers
from helpers.widgets_helpers import WidgetHelpers
from views.insert_payment_view import InsertPayment
from ui.ui_cards import Ui_MainWindow
from views.card_management_view import CardsManagement
from components.dialog_window import DialogWindow


class Cards(QMainWindow):
    today = datetime.today()
    qdate = QDate(today.year, today.month, today.day)

    def __init__(self, logged_user: dict) -> None:
        super(Cards, self).__init__()
        self.ui = Ui_MainWindow()  # instanciar a classe Ui_MainWindow
        self.ui.setupUi(self)
        self.setWindowTitle(f"Cartões {os.getenv('COMPANY')} | Lançamento")
        self.logged_user = logged_user
        self.is_admin_user = self.logged_user["adminUser"]
        self.orders_data = None
        self.fetch_and_load_orders()
        self.disable_search_button()
        self.manage_user_permission()
        self.details_window = None
        self.add_payment_window = None
        self.cards_management_window = None
        self.dialog_window = DialogWindow()
        self.ui.tableWidget.setColumnWidth(2, 88)  # Definindo a largura da coluna da data para 88 pixels
        self.connect_button_actions()
        self.connect_text_changes()
        self.install_event_filters()
        self.ui.initial_date.setDate(self.qdate)
        self.ui.final_date.setDate(self.qdate)

    def install_event_filters(self) -> None:
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
        WidgetHelpers.connect_texts_changes(self, self.manage_search_button)

    def load_orders_table(self, data: list) -> None:

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

        if self.is_admin_user:
            self.enable_admin_buttons()
        else:
            self.disable_admin_button()

    def fetch_user_orders(self) -> None:

        if self.is_admin_user:
            self.orders_data = RepositoryManager.order_stage_repository().get_uncommited_orders(
                self.logged_user["store"])
        else:
            self.orders_data = RepositoryManager.order_stage_repository().get_uncommited_orders(
                self.logged_user["store"],
                self.logged_user["userCode"])

    def fetch_and_load_orders(self) -> None:
        self.fetch_user_orders()
        self.load_orders_table(self.orders_data)

    def get_filtered_order(self, order_number) -> list:

        if self.is_admin_user:
            data = RepositoryManager.order_stage_repository().filter_uncommited_order(self.logged_user["store"],
                                                                                      order_number)
        else:
            data = RepositoryManager.order_stage_repository().filter_uncommited_order(self.logged_user["store"],
                                                                                      order_number,
                                                                                      self.logged_user["userCode"])

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

        cell_click = self.ui.tableWidget.item(row, 0).row()  # pega o valor da coluna "Pedido"

        uid = self.orders_data[cell_click][-1]
        self.details_window = CardDetails(uid, self.logged_user["adminUser"], self.logged_user["store"])
        self.details_window.show()
        self.details_window.closed.connect(self.fetch_and_load_orders)

    def handle_add_payment_button(self) -> None:
        self.add_payment_window = InsertPayment()
        self.add_payment_window.clear_fields()
        self.add_payment_window.show()
        self.add_payment_window.closed.connect(self.fetch_and_load_orders)

    def handle_report_button(self) -> None:
        initial_date = DateHelpers.to_sql_format(self.ui.initial_date.text())
        final_date = DateHelpers.to_sql_format(self.ui.final_date.text())

        options = {
            "select": "orderNumber, cashierNumber, cashFlow, transactionType, flag, installments, installmentValue, "
                      "orderValue, purchaseDate, NSU, transactionAuthorization",
            "distinct": True,
            "query": {
                "cashierNumber": self.logged_user["userCode"],
                "initial_date": initial_date,
                "final_date": final_date
            },
            "order_by": ["flag"]
        }

        orders = RepositoryManager.checked_orders_repository().get_all(options)
        generate_conference_report(orders)

    def handle_management_button(self) -> None:
        self.cards_management_window = CardsManagement()
        self.cards_management_window.show()
        self.cards_management_window.closed.connect(self.fetch_and_load_orders)

    def handle_search_button(self) -> None:
        self.load_filtered_order()
        self.clear_fields()

    def handle_refresh_button(self) -> None:
        self.fetch_and_load_orders()

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
    window = Cards({"userCode": 15, "adminUser": True, "store": 5})
    window.show()
    app.exec()
