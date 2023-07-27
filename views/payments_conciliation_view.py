import os
from os import getlogin
from os.path import exists

from PySide6.QtWidgets import *

from config.setup_config import setup_config
from database.repositories.repository_manager import RepositoryManager
from helpers.date_helpers import DateHelpers

from ui.ui_payments_conciliation import Ui_MainWindow
from views.quick_management_view import QuickManagement
from views.receiving_view import Receiving
from components.dialog_window_manager import DialogWindowManager
from carrier_excel import CarrierExcel
from helpers.widgets_helpers import WidgetHelpers
from reports.report_manager import ReportManager

setup_config()


class PaymentsConciliation(QMainWindow):

    def __init__(self) -> None:
        super(PaymentsConciliation, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.found_payments = None
        self.old_found_payments = None
        self.not_found_payments = None
        self.unconciliated_payments = None
        self.old_unconciliated = None
        self.payment_receiving_window = None
        self.connect_widget_actions()
        self.set_current_date()
        self.disable_conciliate_button()
        self.disable_excel_button()
        self.file_path = fr"c:\users\{getlogin()}\desktop\recebimentocielo.xlsx"
        self.setWindowTitle(f"{os.getenv('COMPANY')} | Conciliação de pagamentos")
        self.quick_management_window = None

    def verify_file(self):

        if exists(self.file_path):
            WidgetHelpers.manage_buttons(self, set_disabled=True)
            self.retrieve_carrier_payments()
        else:
            DialogWindowManager.dialog().file_not_found(f"O arquivo {self.file_path} não foi encontrado!")

    def retrieve_carrier_payments(self):
        WidgetHelpers.manage_buttons(self, set_disabled=True)
        carrier_excel = CarrierExcel(self.file_path)
        carrier_excel.load_carrier_payments({"initial_date": self.ui.conciliation_initial_date.text(),
                                             "final_date": self.ui.conciliation_final_date.text()
                                             })
        self.old_found_payments, self.found_payments, self.not_found_payments = carrier_excel.find_payments()
        WidgetHelpers.manage_buttons(self, set_disabled=False)
        self.manage_conciliation_tables()

    def load_new_payments_payments(self) -> None:
        data = self.found_payments

        num_rows = len(data)
        num_columns = len(data[0]) - 2

        self.ui.new_table.setRowCount(num_rows)
        self.ui.new_table.setColumnCount(num_columns)

        for row, payment in enumerate(data):
            for col, value in enumerate(payment.values()):
                if col == 1:
                    value = 'Crédito' if value == 'credit' else 'Débito'
                if col == 4 or col == 9:
                    value = f"R$ {round(value, 2)}"
                if col == 6 or col == 7:
                    value = DateHelpers.to_default_format(value)
                item = QTableWidgetItem(str(value))
                self.ui.new_table.setItem(row, col, item)
        self.ui.new_table.resizeColumnsToContents()

    def load_old_payments(self) -> None:
        data = self.old_found_payments

        num_rows = len(data)
        num_columns = len(data[0]) - 2

        self.ui.old_table.setRowCount(num_rows)
        self.ui.old_table.setColumnCount(num_columns)

        for row, payment in enumerate(data):
            for col, value in enumerate(payment.values()):
                if col == 0:
                    value = DateHelpers.to_default_format(value)
                if col == 2:
                    value = f"R$ {round(value, 2)}"
                item = QTableWidgetItem(str(value))
                self.ui.old_table.setItem(row, col, item)
        self.ui.old_table.resizeColumnsToContents()

    def load_not_found_payments(self):
        data = self.not_found_payments

        num_rows = len(data)
        num_columns = len(data[0]) - 2

        self.ui.not_found_table.setRowCount(num_rows)
        self.ui.not_found_table.setColumnCount(num_columns)

        for row, payment in enumerate(data):
            for col, value in enumerate(payment.values()):
                if col == 2 or col == 4:
                    value = DateHelpers.to_default_format(value)
                if col == 7:
                    value = f"R$ {round(float(value), 2)}"
                item = QTableWidgetItem(str(value))
                self.ui.not_found_table.setItem(row, col, item)
        self.ui.not_found_table.resizeColumnsToContents()

    def set_payments_count(self) -> None:
        payments_count = [len(self.found_payments), len(self.old_found_payments), len(self.not_found_payments)]

        for index in range(self.ui.conciliation_tab.count()):
            tab_name = self.ui.conciliation_tab.tabText(index)
            self.ui.conciliation_tab.setTabText(index, f"{tab_name} ({payments_count[index]})")

        self.ui.total_conciliation_label.setText(f"Total de pagamentos: {sum(payments_count)}")

    def set_conciliation_values(self):
        total_conciliation_values = [sum(payment["installmentValue"] for payment in self.found_payments),
                                     sum(payment["installmentValue"] for payment in self.old_found_payments),
                                     sum(payment["installmentValue"] for payment in self.not_found_payments)]

        for index in range(self.ui.conciliation_tab.count()):
            tab_name = self.ui.conciliation_tab.tabText(index)
            self.ui.conciliation_tab.setTabText(index, f"{tab_name} R$ {round(total_conciliation_values[index], 2)}")

    def manage_conciliation_tables(self) -> None:
        self.clear_conciliation_cound()
        self.clear_conciliated_labels()
        self.clear_conciliate_tables()

        if self.old_found_payments:
            self.load_old_payments()
        if self.found_payments:
            self.load_new_payments_payments()
        if self.not_found_payments:
            self.load_not_found_payments()

        self.set_payments_count()
        self.set_conciliation_values()

    def load_unconciliated(self) -> None:

        data = self.unconciliated_payments

        num_rows = len(data)
        num_columns = len(data[0]) - 1

        self.ui.unconciliated_table.setRowCount(num_rows)
        self.ui.unconciliated_table.setColumnCount(num_columns)

        for row, order in enumerate(data):
            for col, value in enumerate(order):
                if col == 1:
                    value = 'Crédito' if value == 'credit' else 'Débito'
                if col == 4 or col == 9:
                    value = f"R$ {round(value, 2)}"
                if col == 6 or col == 7:
                    value = DateHelpers.to_default_format(value)
                self.ui.unconciliated_table.setItem(row, col, QTableWidgetItem(str(value)))

        self.ui.unconciliated_table.resizeColumnsToContents()

    def load_old_unconciliated(self) -> None:

        data = self.old_unconciliated

        num_rows = len(data)
        num_columns = len(data[0]) - 1

        self.ui.old_unconciliated_table.setRowCount(num_rows)
        self.ui.old_unconciliated_table.setColumnCount(num_columns)

        for row, order in enumerate(data):
            for col, value in enumerate(order):
                if col == 0:
                    value = DateHelpers.to_default_format(value)
                if col == 2:
                    value = f"R$ {round(value, 2)}"
                self.ui.old_unconciliated_table.setItem(row, col, QTableWidgetItem(str(value)))

        self.ui.old_unconciliated_table.resizeColumnsToContents()

    def set_unconciliated_count(self) -> None:
        payments_count = [len(self.unconciliated_payments), len(self.old_unconciliated)]

        for index in range(self.ui.unconciliated_tab.count()):
            tab_name = self.ui.unconciliated_tab.tabText(index)
            self.ui.unconciliated_tab.setTabText(index, f"{tab_name} ({payments_count[index]})")

        self.ui.total_unconciliated_label.setText(f"Total de pagamentos não conciliados: {sum(payments_count)}")

    def set_unconciliated_values(self):
        total_unconciliated_values = [
            sum(round(payment[4], 2) for payment in self.unconciliated_payments),
            sum(round(payment[2], 2) for payment in self.old_unconciliated),
        ]

        for index in range(self.ui.unconciliated_tab.count()):
            tab_name = self.ui.unconciliated_tab.tabText(index)
            self.ui.unconciliated_tab.setTabText(index, f"{tab_name} R$ {total_unconciliated_values[index]}")

    def manage_unconciliated_tables(self) -> None:
        self.clear_unconciliated_count()
        self.clear_unconciliated_labels()
        self.clear_unconciliated_tables()

        date_period = {'initial_date': DateHelpers.to_sql_format(self.ui.unconciliated_initial_date.text()),
                       'final_date': DateHelpers.to_sql_format(self.ui.unconciliated_final_date.text())}

        self.unconciliated_payments = RepositoryManager.checked_orders_repository().get_unconciliated_orders(
            date_period)

        self.old_unconciliated = RepositoryManager.old_payments_repository().get_unconciliated_orders(
            date_period)

        if self.unconciliated_payments:
            self.load_unconciliated()
        if self.old_unconciliated:
            self.load_old_unconciliated()

        self.set_unconciliated_count()
        self.set_unconciliated_values()

    def generate_unconciliated_report(self) -> None:
        ReportManager.unconciliateds().generate((self.unconciliated_payments, self.old_unconciliated))

    def set_current_date(self):
        WidgetHelpers.set_current_date(self)

    def enable_conciliate_button(self) -> None:
        self.ui.conciliate_button.setDisabled(False)

    def disable_conciliate_button(self) -> None:
        self.ui.conciliate_button.setDisabled(True)

    def enable_excel_button(self) -> None:
        self.ui.excel_button.setDisabled(False)

    def disable_excel_button(self) -> None:
        self.ui.excel_button.setDisabled(True)

    def manage_conciliate_button(self) -> None:

        if self.found_payments or self.old_found_payments:
            self.enable_conciliate_button()
        else:
            self.disable_conciliate_button()

    def manage_excel_button(self) -> None:

        if self.unconciliated_payments or self.old_unconciliated:
            self.enable_excel_button()
        else:
            self.disable_excel_button()

    def handle_payment_status_button(self) -> None:
        if self.payment_receiving_window is None:
            self.payment_receiving_window = Receiving()
            self.payment_receiving_window.show()
        else:
            self.payment_receiving_window.show()

    def conciliate_payments(self):
        for payment in self.found_payments:
            RepositoryManager.checked_orders_repository().conciliate_orders(
                {"payday": payment["payday"],
                 "currentInstallment": payment["currentInstallment"],
                 "status": payment["status"],
                 "uId": payment["uId"]}
            )

    def conciliate_old_payments(self):
        for payment in self.old_found_payments:
            RepositoryManager.old_payments_repository().conciliate_orders(
                {"payday": payment["payday"],
                 "currentInstallment": payment["currentInstallment"],
                 "status": payment["status"],
                 "uId": payment["uId"]}
            )

    def manage_conciliations(self):
        current_index = self.ui.conciliation_tab.currentIndex()

        if current_index == 0:
            self.conciliate_payments()

        if current_index == 1:
            self.conciliate_old_payments()

        self.sucess_dialog(current_index)
        self.retrieve_carrier_payments()

    def sucess_dialog(self, tab_index) -> None:

        tabs = {0:
                    {"payments_quantity": len(self.found_payments),
                     "tab_name": "Pagamentos atuais"},
                1: {"payments_quantity": len(self.old_found_payments),
                    "tab_name": "Pagamentos conexão"}
                }

        DialogWindowManager.dialog().successful_conciliation(
            f"{tabs[tab_index]['payments_quantity']} {tabs[tab_index]['tab_name']} conciliados com sucesso!")

    def clear_conciliate_tables(self) -> None:
        conciliation_tables = [self.ui.old_table, self.ui.new_table, self.ui.not_found_table]

        for table in conciliation_tables:
            table.clearContents()
            table.setRowCount(0)

    def clear_unconciliated_tables(self) -> None:
        unconciliated_tables = [self.ui.unconciliated_table, self.ui.old_unconciliated_table]

        for table in unconciliated_tables:
            table.clearContents()
            table.setRowCount(0)

    def clear_conciliated_labels(self):
        self.ui.total_conciliation_label.setText("")

    def clear_unconciliated_labels(self):
        self.ui.total_unconciliated_label.setText("")

    def clear_unconciliated_count(self):
        unconciliated_tabs = ["Não conciliados atuais", "Não conciliados conexão"]

        for index in range(self.ui.unconciliated_tab.count()):
            self.ui.unconciliated_tab.setTabText(index, unconciliated_tabs[index])

    def clear_conciliation_cound(self):
        conciliation_tabs = ["Pagamentos atuais", "Pagamentos conexão", "Pagamentos não encontrados"]

        for index in range(self.ui.conciliation_tab.count()):
            self.ui.conciliation_tab.setTabText(index, conciliation_tabs[index])

    def clear_widgets(self):
        self.clear_conciliation_cound()
        self.clear_unconciliated_count()
        self.clear_conciliated_labels()
        self.clear_unconciliated_labels()
        self.clear_conciliate_tables()
        self.clear_unconciliated_tables()
        self.disable_conciliate_button()
        self.disable_excel_button()
        self.set_current_date()

    def connect_widget_actions(self):
        self.ui.conciliation_search_button.clicked.connect(self.verify_file)
        self.ui.conciliation_search_button.clicked.connect(self.manage_conciliate_button)
        self.ui.unconciliated_search_button.clicked.connect(self.manage_unconciliated_tables)
        self.ui.unconciliated_search_button.clicked.connect(self.manage_excel_button)
        self.ui.clear_button.clicked.connect(self.clear_widgets)
        self.ui.conciliate_button.clicked.connect(self.manage_conciliations)
        self.ui.unconciliated_table.cellDoubleClicked.connect(self.handle_cell_double_click)
        self.ui.old_unconciliated_table.cellDoubleClicked.connect(self.handle_cell_double_click)
        self.ui.excel_button.clicked.connect(self.generate_unconciliated_report)
        self.ui.payments_status_button.clicked.connect(self.handle_payment_status_button)

    def handle_cell_double_click(self, row):
        selecte_tab = self.ui.unconciliated_tab.currentIndex()
        quick_management_data = {}

        tabs = {0: {
            "tab_table": self.ui.unconciliated_table,
            "payments": self.unconciliated_payments},
            1: {
            "tab_table": self.ui.old_unconciliated_table,
            "payments": self.old_unconciliated}
        }

        clicked_row = tabs[selecte_tab]["tab_table"].item(row, 0).row()

        if selecte_tab == 0:
            quick_management_data = {
                "NSU": tabs[selecte_tab]["payments"][clicked_row][10],
                "transactionAuthorization": tabs[selecte_tab]["payments"][clicked_row][11],
                "uId": tabs[selecte_tab]["payments"][clicked_row][13],
                "repository": "checkedOrders"
            }
        if selecte_tab == 1:
            quick_management_data = {
                "NSU": tabs[selecte_tab]["payments"][clicked_row][5],
                "transactionAuthorization": tabs[selecte_tab]["payments"][clicked_row][6],
                "uId": tabs[selecte_tab]["payments"][clicked_row][8],
                "repository": "oldPayments"
            }

        self.quick_management_window = QuickManagement(quick_management_data)
        self.quick_management_window.show()
        self.quick_management_window.closed.connect(self.manage_unconciliated_tables)


if __name__ == "__main__":
    app = QApplication()
    window = PaymentsConciliation()
    window.show()
    app.exec()

# USE card_payments_dev
#
#
# ALTER TABLE checkedOrders
# ADD [conciliated][BIT] DEFAULT 0
#
# ALTER TABLE oldPayments
# ADD [uId][VARCHAR](36)
#
# ALTER TABLE oldPayments
# ADD [conciliated][BIT] DEFAULT 0
#
#
#
# SELECT * FROM checkedOrders
# SELECT * FROM oldPayments
#
#
# UPDATE checkedOrders
# SET conciliated = 0
# WHERE conciliated IS NULL
#
#
# UPDATE oldPayments
# SET conciliated = 0
# WHERE conciliated IS NULL
