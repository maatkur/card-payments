import sys
from datetime import datetime
from PySide6 import QtCore
from PySide6.QtWidgets import *
from PySide6.QtCore import Signal, QDate
from ui.ui_insert_payment import Ui_Form
from database.repositories.repository_manager import RepositoryManager
from helpers.date_helpers import DateHelpers
from helpers.widgets_helpers import WidgetHelpers
from helpers.uuid_helpers import UuidHelpers

from config.setup_config import setup_config

setup_config()


class InsertPayment(QMainWindow):
    closed = Signal()
    today = datetime.today()
    qdate = QDate(today.year, today.month, today.day)

    def __init__(self) -> None:
        super(InsertPayment, self).__init__()
        self.ui = Ui_Form()  # instanciar a classe Ui_form
        self.ui.setupUi(self)
        self.setWindowTitle("Inserir pagamento")
        self.ui.order_date.setDate(self.qdate)
        self.ui.order_entry.setFocus()
        self._setup_window_config()

    def _setup_window_config(self):
        self.install_event_filters()
        self.connect_widgets_actions()
        self.connect_texts_changes()
        self.fill_stores_combo_box()
        self.disable_save_button()

    def install_event_filters(self) -> None:
        self.ui.order_entry.installEventFilter(self)
        self.ui.cashier_entry.installEventFilter(self)
        self.ui.cashflow_entry.installEventFilter(self)
        self.ui.order_value_entry.installEventFilter(self)
        self.ui.order_date.installEventFilter(self)

    def eventFilter(self, widget, event) -> bool:
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

        return False

    def connect_widgets_actions(self) -> None:
        self.ui.save_button.clicked.connect(self.handle_save_button)
        self.ui.stores_comboBox.currentIndexChanged.connect(self.allow_save_button_use)

    def connect_texts_changes(self) -> None:
        WidgetHelpers.connect_texts_changes(self, self.allow_save_button_use)

    def insert_payment(self) -> None:
        order_numer = self.ui.order_entry.text()
        cashier_number = self.ui.cashier_entry.text()
        cash_flow = self.ui.cashflow_entry.text()
        order_value = self.ui.order_value_entry.text().replace(",", ".")
        order_date = DateHelpers.to_sql_format(self.ui.order_date.text())
        store = self.ui.stores_comboBox.currentText()

        order = {"orderNumber": order_numer,
                 "cashierNumber": cashier_number,
                 "cashFlow": cash_flow,
                 "orderValue": order_value,
                 "storeUnit": store,
                 "dateUpdate": order_date,
                 "isCommit": "0",
                 "uId": UuidHelpers.generate_uuid()}

        RepositoryManager.order_stage_repository().insert(order)

    def handle_save_button(self) -> None:
        self.insert_payment()
        self.close_window()

    def clear_fields(self):
        self.ui.order_entry.setFocus()
        self.ui.order_entry.setText("")
        self.ui.cashier_entry.setText("")
        self.ui.cashflow_entry.setText("")
        self.ui.order_value_entry.setText("")
        self.ui.order_date.setDate(self.qdate)

    def store_getter(self) -> list:

        stores = RepositoryManager.stores_repository().get_all_stores()

        return stores

    def fill_stores_combo_box(self):
        stores = self.store_getter()
        for store in stores:
            self.ui.stores_comboBox.addItem(store)

    def allow_save_button_use(self):
        store_was_selected = self.ui.stores_comboBox.currentText() != "Selecione"
        line_edits_filleds = WidgetHelpers.line_edits_filled(self)

        if store_was_selected and line_edits_filleds:
            self.enable_save_button()
        else:
            self.disable_save_button()

    def disable_save_button(self):
        self.ui.save_button.setDisabled(True)

    def enable_save_button(self):
        self.ui.save_button.setDisabled(False)

    def close_window(self) -> None:
        self.closed.emit()
        self.deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InsertPayment()
    window.show()
    app.exec()
