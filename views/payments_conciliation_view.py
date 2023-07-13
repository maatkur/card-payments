from datetime import datetime

from PySide6.QtCore import QDate
from PySide6.QtWidgets import *

from config.setup_config import setup_config
from database.repositories.repository_manager import RepositoryManager
from helpers.date_helpers import DateHelpers
from helpers.widgets_helpers import WidgetHelpers
from match_payments import match_payments
from ui.untitled import Ui_MainWindow


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
        self.connect_buttons_actions()
        self.set_current_date()

    def load_new_payments_payments(self) -> None:
        data = self.found_payments

        num_rows = len(data)
        num_columns = len(data[0]) - 1

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

    def load_old_payments(self) -> None:
        data = self.old_found_payments

        num_rows = len(data)
        num_columns = len(data[0])

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

    def set_payments_count(self) -> None:
        payments_count = [len(self.found_payments), len(self.old_found_payments), len(self.not_found_payments)]

        for index in range(self.ui.conciliation_tab.count()):
            tab_name = self.ui.conciliation_tab.tabText(index)
            self.ui.conciliation_tab.setTabText(index, f"{tab_name} ({payments_count[index]})")

        self.ui.total_conciliation_label.setText(f"Total de pagamentos: {sum(payments_count)}")

    def manage_conciliation_tables(self) -> None:
        self.old_found_payments, self.found_payments, self.not_found_payments = match_payments()

        if self.old_found_payments:
            self.load_old_payments()
        if self.found_payments:
            self.load_new_payments_payments()
        if self.not_found_payments:
            self.load_not_found_payments()

        self.set_payments_count()

    def load_unconciliated(self) -> None:
        date_period = {'initial_date': DateHelpers.to_sql_format(self.ui.unconciliated_initial_date.text()),
                       'final_date': DateHelpers.to_sql_format(self.ui.unconciliated_final_date.text())}

        self.unconciliated_payments = RepositoryManager.checked_orders_repository().get_unconciliated_orders(
                                            date_period)

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

    def load_old_unconciliated(self) -> None:

        data = self.old_unconciliated

        num_rows = len(data)
        num_columns = len(data[0])

        self.ui.old_unconciliated_table.setRowCount(num_rows)
        self.ui.old_unconciliated_table.setColumnCount(num_columns)

        for row, order in enumerate(data):
            for col, value in enumerate(order):
                if col == 0:
                    value = DateHelpers.to_default_format(value)
                if col == 2:
                    value = f"R$ {round(value, 2)}"
                self.ui.old_unconciliated_table.setItem(row, col, QTableWidgetItem(str(value)))

    def set_unconciliated_count(self) -> None:
        payments_count = [len(self.unconciliated_payments), len(self.old_unconciliated)]

        for index in range(self.ui.unconciliated_tab.count()):
            tab_name = self.ui.unconciliated_tab.tabText(index)
            self.ui.unconciliated_tab.setTabText(index, f"{tab_name} ({payments_count[index]})")

        self.ui.total_unconciliated_label.setText(f"Total de pagamentos não conciliados: {sum(payments_count)}")

    def manage_unconciliated_tables(self) -> None:

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

    def clear_labes_count(self):
        labels_widgets = [self.ui.total_conciliation_label, self.ui.total_unconciliated_label]

        for label in labels_widgets:
            label.setText("")

    def clear_tabs_count(self):
        conciliation_tabs = ["Pagamentos atuais", "Pagamentos conexão", "Pagamentos não encontrados"]
        unconciliated_tabs = ["Não conciliados atuais", "Não conciliados conexão"]

        for index in range(self.ui.conciliation_tab.count()):
            self.ui.conciliation_tab.setTabText(index, conciliation_tabs[index])

        for index in range(self.ui.unconciliated_tab.count()):
            self.ui.unconciliated_tab.setTabText(index, unconciliated_tabs[index])

    def set_current_date(self):
        today = datetime.today()
        qdate = QDate(today.year, today.month, today.day)

        self.ui.excel_initial_date.setDate(qdate)
        self.ui.unconciliated_initial_date.setDate(qdate)
        self.ui.unconciliated_final_date.setDate(qdate)

    def clear_widgets(self):
        self.clear_tabs_count()
        self.clear_labes_count()
        self.set_current_date()
        WidgetHelpers.clear_table(window)

    def connect_buttons_actions(self):
        self.ui.excel_search_button.clicked.connect(self.manage_conciliation_tables)
        self.ui.unconciliated_search_button.clicked.connect(self.manage_unconciliated_tables)
        self.ui.clear_button.clicked.connect(self.clear_widgets)


if __name__ == "__main__":
    app = QApplication()
    window = PaymentsConciliation()
    window.show()
    app.exec()
