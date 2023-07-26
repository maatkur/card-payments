from os import getenv, getlogin
import sys

from PySide6.QtGui import QColor
from PySide6.QtWidgets import *

from ui.ui_receiving import Ui_MainWindow

from carrier_excel import CarrierExcel
from database.repositories.repository_manager import RepositoryManager
from helpers.date_helpers import DateHelpers
from helpers.widgets_helpers import WidgetHelpers
from config.setup_config import setup_config
from reports.report_manager import ReportManager

setup_config()


class Receiving(QMainWindow):

    def __init__(self) -> None:
        super(Receiving, self).__init__()
        self.ui = Ui_MainWindow()  # instanciar a classe Ui_MainWindow
        self.ui.setupUi(self)
        self.setWindowTitle(f"Cartões {getenv('COMPANY')} | Recebimento")
        self.checked_orders = None
        self.old_payments = None
        self.set_current_date()
        self.conect_buttons_actions()
        self.disable_excel_button()
        self.disable_update_button()
        self.file_path = fr"c:\users\{getlogin()}\desktop\recebimentocielo.xlsx"
        self.tabs_options = None

    def create_tabs_options(self):
        self.tabs_options = {
            0: {
                "tab_name": "Pagamentos atuais",
                "payments_count": len(self.checked_orders),
                "total_value": sum(payment[4] for payment in self.checked_orders)
            },
            1: {
                "tab_name": "Pagamentos conexão",
                "payments_count": len(self.old_payments),
                "total_value": sum(payment[2] for payment in self.old_payments)
            }
        }

    def retrieve_conciliated_orders(self) -> None:
        date_period = {
            "initial_date": DateHelpers.to_sql_format(self.ui.initial_date.text()),
            "final_date": DateHelpers.to_sql_format(self.ui.final_date.text())
        }

        self.checked_orders = RepositoryManager.checked_orders_repository().get_conciliateds(date_period)
        self.old_payments = RepositoryManager.old_payments_repository().get_conciliateds(date_period)

    def load_new_table(self):
        # Obtém o status selecionado no combobox
        selected_status = self.ui.status_combo_box.currentText().lower()

        # Filtra os dados com base no status selecionado
        filtered_orders = self.checked_orders

        if selected_status != "todos":
            filtered_orders = [order for order in self.checked_orders if order[12].lower() == selected_status]
        self.tabs_options[0]["payments_count"] = len(filtered_orders)
        self.tabs_options[0]["total_value"] = sum(payment[4] for payment in filtered_orders)

        self.ui.new_table.clearContents()
        self.ui.new_table.setRowCount(0)

        # Limpa a tabela antes de carregar novos dados

        if filtered_orders:

            num_rows = len(filtered_orders)
            num_columns = len(filtered_orders[0]) - 1
            self.ui.new_table.setRowCount(num_rows)
            self.ui.new_table.setColumnCount(num_columns)

            for row, order in enumerate(filtered_orders):
                for col, value in enumerate(order):
                    if col == 1:
                        value = 'Crédito' if value == 'credit' else 'Débito'
                    if col == 4 or col == 9:
                        value = f"R$ {round(value, 2)}"
                    if col == 6 or col == 7:
                        value = DateHelpers.to_default_format(value)
                    item = QTableWidgetItem(str(value))
                    self.ui.new_table.setItem(row, col, item)
                status_index = 12  # Substitua pelo índice correto do status no seu conjunto de dados
                status = order[status_index]
                if status.lower() == "indefinido":
                    for col in range(self.ui.new_table.columnCount()):
                        self.ui.new_table.item(row, col).setBackground(QColor(255, 152, 154))  # Verde
                if status.lower() == "agendado":
                    for col in range(self.ui.new_table.columnCount()):
                        self.ui.new_table.item(row, col).setBackground(QColor(254, 255, 197))  # Verde
                if status.lower() == "enviado banco":
                    for col in range(self.ui.new_table.columnCount()):
                        self.ui.new_table.item(row, col).setBackground(QColor(208, 255, 169))  # Verde
                if status.lower() == "pago":
                    for col in range(self.ui.new_table.columnCount()):
                        self.ui.new_table.item(row, col).setBackground(QColor(0, 255, 0))  # Verde

            self.ui.new_table.resizeColumnsToContents()

    def load_old_table(self) -> None:
        # Obtém o status selecionado no combobox
        selected_status = self.ui.status_combo_box.currentText().lower()

        # Filtra os dados com base no status selecionado
        filtered_orders = self.old_payments
        if selected_status != "todos":
            filtered_orders = [order for order in self.old_payments if order[7].lower() == selected_status]
        self.tabs_options[1]["payments_count"] = len(filtered_orders)
        self.tabs_options[1]["total_value"] = sum(payment[2] for payment in filtered_orders)

        self.ui.old_table.clearContents()
        self.ui.old_table.setRowCount(0)

        if filtered_orders:
            num_rows = len(filtered_orders)
            num_columns = len(filtered_orders[0]) - 1

            self.ui.old_table.setRowCount(num_rows)
            self.ui.old_table.setColumnCount(num_columns)

            for row, order in enumerate(filtered_orders):
                for col, value in enumerate(order):
                    if col == 0:
                        value = DateHelpers.to_default_format(value)
                    if col == 2:
                        value = f"R$ {round(value, 2)}"
                    item = QTableWidgetItem(str(value))
                    self.ui.old_table.setItem(row, col, item)

                status_index = 7
                status = order[status_index]
                if status.lower() == "indefinido":
                    for col in range(self.ui.new_table.columnCount()):
                        self.ui.old_table.item(row, col).setBackground(QColor(255, 152, 154))
                if status.lower() == "agendado":
                    for col in range(self.ui.old_table.columnCount()):
                        self.ui.old_table.item(row, col).setBackground(QColor(254, 255, 197))
                if status.lower() == "enviado banco":
                    for col in range(self.ui.old_table.columnCount()):
                        self.ui.old_table.item(row, col).setBackground(QColor(208, 255, 169))
                if status.lower() == "pago":
                    for col in range(self.ui.old_table.columnCount()):
                        self.ui.old_table.item(row, col).setBackground(QColor(0, 255, 0))

            self.ui.old_table.resizeColumnsToContents()

    def manage_tables(self):

        if self.checked_orders:
            self.load_new_table()
        if self.old_payments:
            self.load_old_table()

    def retrive_and_manage(self):
        WidgetHelpers.clear_table(self)
        self.retrieve_conciliated_orders()
        self.create_tabs_options()
        self.manage_tables()
        self.load_tabs_options()

    def enable_excel_button(self) -> None:
        self.ui.excel_button.setDisabled(False)

    def disable_excel_button(self) -> None:
        self.ui.excel_button.setDisabled(True)

    def update_excel_and_buttons_state(self) -> None:

        if self.checked_orders or self.old_payments:
            self.enable_excel_button()
            self.enable_update_button()
        else:
            self.disable_excel_button()
            self.disable_update_button()

    def enable_update_button(self) -> None:
        self.ui.update_button.setDisabled(False)

    def disable_update_button(self) -> None:
        self.ui.update_button.setDisabled(True)


    def load_carrier_status(self):
        carrier_excel = CarrierExcel(self.file_path)
        carrier_excel.load_carrier_payments({"initial_date": self.ui.initial_date.text(),
                                             "final_date": self.ui.final_date.text()
                                             })
        return carrier_excel.find_payments_status()

    def update_payments_status(self, payments_status):
        for status in payments_status:
            RepositoryManager.checked_orders_repository().update_order_status(
                {"uId": status["uId"],
                 "currentInstallment": status["currentInstallment"],
                 "status": status["status"]
                 }
            )

    def update_old_payments_status(self, old_payments_status):
        for status in old_payments_status:
            RepositoryManager.old_payments_repository().update_order_status(
                {"uId": status["uId"],
                 "currentInstallment": status["currentInstallment"],
                 "status": status["status"]
                 }
            )

    def update_orders_status(self):
        payments_status, old_payments_status = self.load_carrier_status()

        self.update_payments_status(payments_status)
        self.update_old_payments_status(old_payments_status)

    def load_tabs_options(self):

        for index in range(self.ui.tabWidget.count()):
            tabs = self.tabs_options[index]
            self.ui.tabWidget.setTabText(index,
                                    f"{tabs['tab_name']} ({tabs['payments_count']}) R$ {round(tabs['total_value'], 2)}")

    def generate_conciliateds_report(self) -> None:
        ReportManager.conciliateds().generate((self.checked_orders, self.old_payments))

    def clear_tabs_options(self):
        for index in range(self.ui.tabWidget.count()):
            tabs = self.tabs_options[index]
            self.ui.tabWidget.setTabText(index, tabs["tab_name"])

    def conect_buttons_actions(self) -> None:
        self.ui.search_button.clicked.connect(self.retrive_and_manage)
        self.ui.search_button.clicked.connect(self.update_excel_and_buttons_state)
        self.ui.clear_button.clicked.connect(self.new_search)
        self.ui.update_button.clicked.connect(self.update_orders_status)
        self.ui.status_combo_box.currentIndexChanged.connect(self.manage_tables)
        self.ui.status_combo_box.currentIndexChanged.connect(self.load_tabs_options)
        self.ui.excel_button.clicked.connect(self.generate_conciliateds_report)

    def set_current_date(self):
        WidgetHelpers.set_current_date(self)

    def new_search(self):
        self.checked_orders = None
        self.old_payments = None
        self.clear_tabs_options()
        self.set_current_date()
        WidgetHelpers.clear_table(self)
        self.disable_update_button()
        self.disable_excel_button()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Receiving()
    window.show()
    app.exec()
