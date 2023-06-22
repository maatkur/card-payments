import sys
from datetime import datetime
from PySide6 import QtCore
from PySide6.QtWidgets import *
from PySide6.QtCore import Signal, QDate
from ui.ui_manual_insert import Ui_Form
from database.db_handler import DatabaseHandler


class AddPayment(QMainWindow):
    closed = Signal()
    today = datetime.today()
    qdate = QDate(today.year, today.month, today.day)

    def __init__(self) -> None:
        super(AddPayment, self).__init__()
        self.ui = Ui_Form()  # instanciar a classe Ui_form
        self.ui.setupUi(self)
        self.db_handler = DatabaseHandler()
        self.setWindowTitle("Inserir pagamento")
        self.ui.order_date.setDate(self.qdate)
        self.db_handler = DatabaseHandler()
        self.fill_stores_combo_box()
        self.ui.order_entry.setFocus()
        self.ui.save_button.clicked.connect(self.handle_save_button)
        self.ui.order_entry.installEventFilter(self)
        self.ui.cashier_entry.installEventFilter(self)
        self.ui.cashflow_entry.installEventFilter(self)
        self.ui.order_value_entry.installEventFilter(self)
        self.ui.order_date.installEventFilter(self)
        self.disable_save_button()
        self.ui.stores_comboBox.currentIndexChanged.connect(self.allow_save_button_use)

    def eventFilter(self, widget, event) -> None:
        if event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            if key == QtCore.Qt.Key_Return or key == QtCore.Qt.Key_Enter:
                if widget == self.ui.order_entry:
                    self.ui.cashier_entry.setFocus()
                if widget == self.ui.cashier_entry:
                    self.ui.cashflow_entry.setFocus()
                if widget == self.ui.cashflow_entry:
                    self.ui.order_value_entry.setFocus()
                if widget == self.ui.order_value_entry:
                    self.ui.order_date.setFocus()
                if widget == self.ui.order_date:
                    self.ui.save_button.setFocus()

    def insert_order_manually(self) -> None:
        order_numer = self.ui.order_entry.text()
        cashier_number = self.ui.cashier_entry.text()
        cash_flow = self.ui.cashflow_entry.text()
        order_value = self.ui.order_value_entry.text().replace(",", ".")
        order_date = self.ui.order_date.text()
        store = self.ui.stores_comboBox.currentText()

        self.db_handler.connect()
        self.db_handler.manually_insert_in_order_stage(order_numer, cashier_number, cash_flow, order_value,
                                                       store, order_date)
        self.db_handler.disconnect()

    def handle_save_button(self) -> None:
        self.insert_order_manually()
        self.close_add_payment_window()

    def clear_fields(self):
        self.ui.order_entry.setFocus()
        self.ui.order_entry.setText("")
        self.ui.cashier_entry.setText("")
        self.ui.cashflow_entry.setText("")
        self.ui.order_value_entry.setText("")
        self.ui.order_date.setDate(self.qdate)

    def store_getter(self) -> list:

        self.db_handler.connect()
        stores = self.db_handler.get_stores()
        self.db_handler.disconnect()

        return stores

    def fill_stores_combo_box(self):
        stores = self.store_getter()
        for store in stores:
            self.ui.stores_comboBox.addItem(store[0])

    def allow_save_button_use(self):
        store_was_selected = self.ui.stores_comboBox.currentText() != "Selecione"
        if store_was_selected:
            self.enable_save_button()
        else:
            self.disable_save_button()

    def disable_save_button(self):
        self.ui.save_button.setDisabled(True)

    def enable_save_button(self):
        self.ui.save_button.setDisabled(False)

    def close_add_payment_window(self) -> None:
        self.closed.emit()
        self.deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddPayment()
    window.show()
    app.exec()
