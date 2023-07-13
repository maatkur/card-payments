import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import QDate

from ui.untitled import Ui_MainWindow

from config.setup_config import setup_config

from datetime import datetime
from match_payments import match_payments

setup_config()


class PaymentsConciliation(QMainWindow):
    today = datetime.today()
    qdate = QDate(today.year, today.month, today.day)

    def __init__(self) -> None:
        super(PaymentsConciliation, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.excel_initial_date.setDate(self.qdate)
        self.ui.unconciliated_initial_date.setDate(self.qdate)
        self.ui.unconciliated_final_date.setDate(self.qdate)
        self.found_payments = None
        self.old_found_payments = None
        self.not_found_payments = None
        self.ui.excel_search_button.clicked.connect(self.load_payments)

    def load_old_payments(self) -> None:
        data = self.old_found_payments

        num_rows = len(data)
        num_columns = len(data[0])

        self.ui.old_table.setRowCount(num_rows)
        self.ui.old_table.setColumnCount(num_columns)

        for row, payment in enumerate(data):
            for col, value in enumerate(payment.values()):
                item = QTableWidgetItem(str(value))
                self.ui.old_table.setItem(row, col, item)

    def load_new_payments_payments(self) -> None:
        data = self.found_payments

        num_rows = len(data)
        num_columns = len(data[0]) - 1

        self.ui.new_table.setRowCount(num_rows)
        self.ui.new_table.setColumnCount(num_columns)

        for row, payment in enumerate(data):
            for col, value in enumerate(payment.values()):
                item = QTableWidgetItem(str(value))
                self.ui.new_table.setItem(row, col, item)

    def load_not_found_payments(self):
        data = self.not_found_payments

        num_rows = len(data)
        num_columns = len(data[0]) - 1

        self.ui.not_found_table.setRowCount(num_rows)
        self.ui.not_found_table.setColumnCount(num_columns)

        for row, payment in enumerate(data):
            for col, value in enumerate(payment.values()):
                item = QTableWidgetItem(str(value))
                self.ui.not_found_table.setItem(row, col, item)

    def load_payments(self) -> None:
        self.old_found_payments, self.found_payments, self.not_found_payments = match_payments()

        if self.old_found_payments:
            self.load_old_payments()
        if self.found_payments:
            self.load_new_payments_payments()
        if self.not_found_payments:
            self.load_not_found_payments()

    def manage_tables(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PaymentsConciliation()
    window.show()
    app.exec()
