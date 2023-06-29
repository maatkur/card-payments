import sys
from datetime import datetime

from PySide6.QtCore import Signal, QDate, Qt, QEvent
from PySide6.QtWidgets import *

from database.repositories.repository_manager import RepositoryManager
from ui.ui_card_management import Ui_Form
from reports.management_report import generate_management_report
from components.dialog_window import DialogWindow
from helpers.date_helpers import DateHelpers
from helpers.order_helpers import OrderHelpers
from config.setup_config import setup_config

setup_config()


class CardsManagement(QMainWindow):
    closed = Signal()
    today = datetime.today()
    qdate = QDate(today.year, today.month, today.day)

    def __init__(self) -> None:
        super(CardsManagement, self).__init__()
        self.ui = Ui_Form()  # instanciar a classe Ui_form
        self.ui.setupUi(self)
        self.setWindowTitle("Manutenção")
        self.dialog_window = DialogWindow()
        self.set_date()
        self.install_event_filters()
        self.fill_stores_combo_box()
        self.set_card_flags()
        self.disable_view_widgets()
        self.connect_button_actions()
        self.table_data = None
        self.clicked_order_data = None

    def install_event_filters(self):
        self.ui.initial_date.installEventFilter(self)
        self.ui.final_date.installEventFilter(self)
        self.ui.order_entry.installEventFilter(self)
        self.ui.search_button.installEventFilter(self)

    def eventFilter(self, widget, event):
        if event.type() == QEvent.KeyPress:
            key = event.key()
            if key == Qt.Key_Return or key == Qt.Key_Enter:
                if widget == self.ui.initial_date:
                    self.ui.final_date.setFocus()
                if widget == self.ui.final_date:
                    self.ui.order_entry.setFocus()
                if widget == self.ui.order_entry:
                    self.ui.search_button.setFocus()
                if widget == self.ui.search_button:
                    self.handle_search_button()
        return False

    def set_data(self, data: list) -> None:
        data = data

        num_rows = len(data)
        num_columns = len(data[0]) - 1

        self.ui.tableWidget.setRowCount(num_rows)
        self.ui.tableWidget.setColumnCount(num_columns)

        for row, order in enumerate(data):
            for col, value in enumerate(order):
                if col == 3 and value == "credit":
                    value = "Crédito"
                if col == 3 and value == "debit":
                    value = "Dédito"
                if col == 5:
                    formatted_value = "{:.2f}".format(round(value, 2))
                    value = formatted_value.replace(".", ",")
                if col == 7:  # verifica se é a coluna da data
                    if isinstance(value, datetime):
                        order_date = value
                    else:
                        order_date = datetime.strptime(value, '%Y-%m-%d')
                    formatted_date = order_date.strftime('%d/%m/%Y')
                    self.ui.tableWidget.setItem(row, col, QTableWidgetItem(formatted_date))
                else:
                    self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(value)))

        self.enable_excel_button()

    def handle_search_button(self) -> None:
        self.get_filtered_orders()
        self.verify_data()

    def get_filtered_orders(self) -> None:
        initial_date = self.ui.initial_date.text()
        final_date = self.ui.final_date.text()
        order_number = self.ui.order_entry.text()
        store_unit = self.ui.stores_comboBox.currentText()

        order_entry_filled = len(order_number) > 0
        store_is_selected = store_unit != "Todas"
        query = {}

        if order_entry_filled:
            query["orderNumber"] = order_number
        else:
            query["initial_date"] = DateHelpers.to_sql_format(initial_date)
            query["final_date"] = DateHelpers.to_sql_format(final_date)
            if store_is_selected:
                query["storeUnit"] = store_unit

        self.table_data = RepositoryManager.checked_orders_repository().get_all_by(query)

    def verify_data(self):
        not_fount = len(self.table_data) == 0

        if not_fount:
            self.dialog_window.not_found()
        else:
            self.set_data(self.table_data)

    def store_getter(self) -> list:

        stores = RepositoryManager.stores_repository().get_all_stores()

        return stores

    def fill_stores_combo_box(self) -> None:
        stores = self.store_getter()
        for store in stores:
            self.ui.stores_comboBox.addItem(store)

    def set_card_flags(self) -> None:

        # Busca as bandeiras de cartões no DB e carrega no combobox

        options = {
            "select": "flag",
            "distinct": True,
            "order_by": ["flag"]
        }

        flags = RepositoryManager.card_flags_repository().get_all(options)

        for flag in flags:
            self.ui.flags_combo_box.addItem(flag[0])

    def handle_cell_double_click(self, row) -> None:
        clicked_row = self.ui.tableWidget.item(row, 0).row()
        uid = self.table_data[clicked_row][-1]
        self.get_clicked_order_data(uid)
        self.fill_view_fields(self.clicked_order_data)
        self.manage_edition_widgets()
        self.connect_text_changes()

    def get_clicked_order_data(self, uid: str) -> None:

        self.clicked_order_data = RepositoryManager.checked_orders_repository().get_first({"uId": uid})

    def fill_view_fields(self, order_data: dict) -> None:
        order_value = round(float(order_data["orderValue"]), 2)
        order_value = str(order_value)

        self.ui.order_view.setText(order_data["orderNumber"])
        self.ui.cashier_view.setText(order_data["cashierNumber"])
        self.ui.value_view.setText(order_value)
        self.ui.cash_flow_view.setText(order_data["cashFlow"])
        self.ui.transaction_view.setText("Crédito" if order_data["transactionType"] == "credit" else "Débito")
        self.ui.flags_combo_box.setCurrentText(order_data["flag"])
        self.ui.installments_combo_box.setCurrentText(order_data["installments"])
        self.ui.nsu_view.setText(order_data["NSU"])
        self.ui.authorization_view.setText(order_data["transactionAuthorization"])

    def enable_excel_button(self) -> None:
        table_filled = self.ui.tableWidget.rowCount() > 0

        if table_filled:
            self.ui.excel_button.setDisabled(False)
        else:
            self.ui.excel_button.setDisabled(True)

    def enable_view_widgets(self) -> None:
        self.ui.value_view.setDisabled(False)
        self.ui.nsu_view.setDisabled(False)
        self.ui.order_view.setDisabled(False)
        self.ui.cashier_view.setDisabled(False)
        self.ui.cash_flow_view.setDisabled(False)
        self.ui.authorization_view.setDisabled(False)
        self.ui.transaction_view.setDisabled(False)
        self.ui.flags_combo_box.setDisabled(False)
        self.ui.installments_combo_box.setDisabled(False)
        self.ui.delete_button.setDisabled(False)
        self.ui.excel_button.setDisabled(False)

    def disable_view_widgets(self) -> None:
        self.ui.value_view.setDisabled(True)
        self.ui.nsu_view.setDisabled(True)
        self.ui.order_view.setDisabled(True)
        self.ui.cashier_view.setDisabled(True)
        self.ui.cash_flow_view.setDisabled(True)
        self.ui.authorization_view.setDisabled(True)
        self.ui.transaction_view.setDisabled(True)
        self.ui.flags_combo_box.setDisabled(True)
        self.ui.installments_combo_box.setDisabled(True)
        self.ui.delete_button.setDisabled(True)
        self.ui.save_button.setDisabled(True)
        self.ui.excel_button.setDisabled(True)

    def set_date(self) -> None:
        self.ui.initial_date.setDate(self.qdate)
        self.ui.final_date.setDate(self.qdate)

    def clear_table(self) -> None:
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)

    def clear_fields(self) -> None:
        widgets = self.findChildren(QLineEdit)
        for widget in widgets:
            if isinstance(widget, QLineEdit):
                widget.clear()

    def manage_edition_widgets(self):
        filled_field = len(self.ui.order_view.text()) > 0

        if filled_field:
            self.enable_view_widgets()
        else:
            self.disable_view_widgets()

    def set_combo_box_default(self) -> None:
        self.ui.stores_comboBox.setCurrentText("Todas")
        self.ui.flags_combo_box.setCurrentText("Selecione")
        self.ui.installments_combo_box.setCurrentText("1")

    def handle_clear_button(self) -> None:
        self.set_date()
        self.clear_fields()
        self.clear_table()
        self.set_combo_box_default()
        self.disable_view_widgets()

    def delete_order(self):

        options = {"uId": self.clicked_order_data["uId"]}
        RepositoryManager.checked_orders_repository().delete(options)

    def uncommit_order(self):
        RepositoryManager.order_stage_repository().uncommit_order(self.clicked_order_data["uId"])

    def handle_delete_button(self):
        title = "Confirmar exclusão"
        message = "Tem certeza que deseja excluir?"

        result = self.dialog_window.confirmation(title, message)

        if result == QMessageBox.Yes:
            self.delete_order()
            self.uncommit_order()
            self.handle_clear_button()

    def update_order_changes(self) -> None:

        changes = self.check_order_changes()
        changes["uId"] = self.clicked_order_data["uId"]

        if changes.get("nsu") or changes.get("transactionAuthorization"):

            RepositoryManager.checked_orders_repository().update(changes)

        elif changes.get("flag") or changes.get("installments"):
            self.delete_order()

            order = self.clicked_order_data
            order["transactionAuthorization"] = self.ui.authorization_view.text()
            order["flag"] = self.ui.flags_combo_box.currentText()
            order["installments"] = self.ui.installments_combo_box.currentText()
            order["transactionType"] = self.ui.transaction_view.text()
            order["nsu"] = self.ui.nsu_view.text()
            order["transactionAuthorization"] = self.ui.authorization_view.text()
            order["flag"] = self.ui.flags_combo_box.currentText()
            order["installments"] = self.ui.installments_combo_box.currentText()

            checked_order = OrderHelpers.create_checked_order(order)

            if type(checked_order) == dict:
                RepositoryManager.checked_orders_repository().insert_debit_order(checked_order)
            else:
                RepositoryManager.checked_orders_repository().inser_credit_order(checked_order)

    def handle_save_button(self):
        title = "Confirmar alterações"
        message = "Tem certeza que deseja salvar as alterações?"

        result = self.dialog_window.confirmation(title, message)

        if result == QMessageBox.Yes:
            self.update_order_changes()
            self.handle_search_button()
            self.disable_save_button()
            self.clear_fields()
            self.disable_view_widgets()

    def manage_save_button(self) -> None:

        changes = self.check_order_changes()

        if changes:
            print(changes)
            self.enable_save_button()
        else:
            self.disable_save_button()

    def check_order_changes(self) -> dict:
        nsu_was_changed = self.clicked_order_data["NSU"] != self.ui.nsu_view.text()
        authorization_was_changed = self.clicked_order_data[
                                        "transactionAuthorization"] != self.ui.authorization_view.text()
        installments_was_changed = self.clicked_order_data[
                                       "installments"] != self.ui.installments_combo_box.currentText()
        flag_was_changed = self.clicked_order_data["flag"] != self.ui.flags_combo_box.currentText()

        changes = {}

        if nsu_was_changed:
            changes["nsu"] = self.ui.nsu_view.text()
        if authorization_was_changed:
            changes["transactionAuthorization"] = self.ui.authorization_view.text()
        if installments_was_changed:
            changes["installments"] = self.ui.installments_combo_box.currentText()
        if flag_was_changed:
            changes["flag"] = self.ui.flags_combo_box.currentText()

        return changes

    def enable_save_button(self) -> None:
        self.ui.save_button.setDisabled(False)

    def disable_save_button(self) -> None:
        self.ui.save_button.setDisabled(True)

    def connect_button_actions(self) -> None:
        self.ui.tableWidget.cellDoubleClicked.connect(self.handle_cell_double_click)
        self.ui.search_button.clicked.connect(self.handle_search_button)
        self.ui.clear_filters_button.clicked.connect(self.handle_clear_button)
        self.ui.delete_button.clicked.connect(self.handle_delete_button)
        self.ui.save_button.clicked.connect(self.handle_save_button)
        self.ui.excel_button.clicked.connect(self.handle_report_button)

    def connect_text_changes(self) -> None:
        self.ui.nsu_view.textChanged.connect(self.manage_save_button)
        self.ui.authorization_view.textChanged.connect(self.manage_save_button)
        self.ui.installments_combo_box.currentTextChanged.connect(self.manage_save_button)
        self.ui.flags_combo_box.currentTextChanged.connect(self.manage_save_button)

    def handle_report_button(self) -> None:
        generate_management_report(self.table_data)

    def close_event(self, event) -> None:
        self.closed.emit()  # emite o sinal closed quando a janela for fechada
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CardsManagement()
    window.show()
    app.exec()
