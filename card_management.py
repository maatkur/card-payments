import sys
from datetime import datetime

from PySide6.QtCore import Signal, QDate, Qt, QEvent
from PySide6.QtWidgets import *

from database.db_handler import DatabaseHandler
from ui.ui_card_management import Ui_Form
from reports.management_report import generate_management_report


class CardsManagement(QMainWindow):
    closed = Signal()
    today = datetime.today()
    qdate = QDate(today.year, today.month, today.day)

    def __init__(self) -> None:
        super(CardsManagement, self).__init__()
        self.ui = Ui_Form()  # instanciar a classe Ui_form
        self.ui.setupUi(self)
        self.setWindowTitle("Manutenção")
        self.db_handler = DatabaseHandler()
        self.set_date()
        self.install_event_filters()
        self.fill_stores_combo_box()
        self.disable_view_widgets()
        self.connect_button_actions()
        self.connect_text_changes()
        self.data = None
        self.nsu = None
        self.authorization = None

    def eventFilter(self, widget, event):
        if event.type() == QEvent.KeyPress:
            key = event.key()
            if key == Qt.Key_Return or key == Qt.Key_Enter:
                if widget == self.ui.initial_date:
                    self.ui.final_date.setFocus()
                if widget == self.ui.final_date:
                    self.ui.order_entry.setFocus()
                if widget == self.ui.order_entry:
                    self.ui.nsu_authorization_entry.setFocus()
                if widget == self.ui.nsu_authorization_entry:
                    self.ui.search_button.setFocus()
                if widget == self.ui.search_button:
                    self.handle_search_button()

    def install_event_filters(self):
        self.ui.initial_date.installEventFilter(self)
        self.ui.final_date.installEventFilter(self)
        self.ui.order_entry.installEventFilter(self)
        self.ui.nsu_authorization_entry.installEventFilter(self)
        self.ui.search_button.installEventFilter(self)

    def set_data(self, data: list) -> None:
        data = data

        num_rows = len(data)
        num_columns = len(data[0])

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
        initial_date = self.ui.initial_date.text()
        final_date = self.ui.final_date.text()
        order = self.ui.order_entry.text()
        nsu_authorization = self.ui.nsu_authorization_entry.text()
        store = self.ui.stores_comboBox.currentText()

        if len(order) == 0:
            order = None
        if len(nsu_authorization) == 0:
            nsu_authorization = None
        if store == "Todas":
            store = None

        self.db_handler.connect()

        self.data = self.db_handler.get_orders_management(order=order, initial_date=initial_date, final_date=final_date,
                                                       nsu_authorization=nsu_authorization, store=store)
        self.set_data(self.data)
        self.db_handler.disconnect()

    def store_getter(self) -> list:

        self.db_handler.connect()
        stores = self.db_handler.get_stores()
        self.db_handler.disconnect()

        return stores

    def fill_stores_combo_box(self):
        stores = self.store_getter()
        for store in stores:
            self.ui.stores_comboBox.addItem(store[0])

    def handle_cell_double_click(self, row) -> None:
        order = self.ui.tableWidget.item(row, 0).text()
        cashier = self.ui.tableWidget.item(row, 1).text()
        cash_flow = self.ui.tableWidget.item(row, 2).text()
        transaction_type = self.ui.tableWidget.item(row, 3).text()
        flag = self.ui.tableWidget.item(row, 4).text()
        order_value = self.ui.tableWidget.item(row, 5).text()
        nsu = self.ui.tableWidget.item(row, 9).text()
        self.nsu = nsu
        authorization = self.ui.tableWidget.item(row, 10).text()
        self.authorization = authorization

        self.ui.order_view.setText(order)
        self.ui.cashier_view.setText(cashier)
        self.ui.cash_flow_view.setText(cash_flow)
        self.ui.transaction_view.setText(transaction_type)
        self.ui.flag_view.setText(flag)
        self.ui.value_view.setText(order_value)
        self.ui.nsu_view.setText(nsu)
        self.ui.authorization_view.setText(authorization)

    def enable_excel_button(self) -> None:
        is_table_filled = self.ui.tableWidget.rowCount() > 0

        if is_table_filled:
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
        self.ui.flag_view.setDisabled(False)
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
        self.ui.flag_view.setDisabled(True)
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

    def set_comboBox_default(self) -> None:
        self.ui.stores_comboBox.setCurrentText("Selecione")

    def handle_clear_button(self) -> None:
        self.set_date()
        self.clear_fields()
        self.clear_table()
        self.set_comboBox_default()
        self.disable_view_widgets()

    def delete_checked_order(self):
        order_number = self.ui.order_view.text()
        self.db_handler.connect()
        self.db_handler.delete_from_checkedOrders(order_number)
        self.db_handler.disconnect()

    def show_confirmation_dialog(self, title, message):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setWindowTitle(title)
        message_box.setText(message)
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        message_box.setDefaultButton(QMessageBox.Cancel)
        result = message_box.exec()

        return result

    def handle_delete_button(self):
        title = "Confirmar exclusão"
        message = "Tem certeza que deseja excluir?"

        result = self.show_confirmation_dialog(title, message)

        if result == QMessageBox.Yes:
            self.delete_checked_order()
            self.handle_clear_button()

    def save_changes(self) -> None:
        new_nsu = self.ui.nsu_view.text()
        new_authorization = self.ui.authorization_view.text()
        order = self.ui.order_view.text()
        old_nsu = self.nsu

        self.db_handler.connect()
        self.db_handler.update_card_docs(new_nsu, new_authorization, order, old_nsu)

        self.db_handler.disconnect()

    def handle_save_button(self):
        title = "Confirmar alterações"
        msg = "Tem certeza que deseja salvar as alterações?"
        result = self.show_confirmation_dialog(title, msg)

        if result == QMessageBox.Yes:
            self.save_changes()
            self.handle_search_button()
            self.disable_save_button()

    def manage_save_button(self):
        authorization_changed = self.ui.authorization_view.text() != self.authorization
        nsu_changed = self.ui.nsu_view.text() != self.nsu

        if authorization_changed or nsu_changed:
            self.enable_save_button()
        else:
            self.disable_save_button()

    def enable_save_button(self):
        self.ui.save_button.setDisabled(False)

    def disable_save_button(self):
        self.ui.save_button.setDisabled(True)

    def connect_button_actions(self):
        self.ui.tableWidget.cellDoubleClicked.connect(self.handle_cell_double_click)
        self.ui.search_button.clicked.connect(self.handle_search_button)
        self.ui.clear_filters_button.clicked.connect(self.handle_clear_button)
        self.ui.delete_button.clicked.connect(self.handle_delete_button)
        self.ui.save_button.clicked.connect(self.handle_save_button)
        self.ui.excel_button.clicked.connect(self.handle_report_button)

    def connect_text_changes(self):
        self.ui.order_view.textChanged.connect(self.manage_edition_widgets)
        self.ui.nsu_view.textChanged.connect(self.manage_save_button)
        self.ui.authorization_view.textChanged.connect(self.manage_save_button)

    def generate_report(self, data: list) -> None:
        generate_management_report(data)

    def handle_report_button(self):
        self.generate_report(self.data)

    def close_details_window(self) -> None:
        self.closed.emit()  # emite o sinal closed quando a janela for fechada
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CardsManagement()
    window.show()
    app.exec()
