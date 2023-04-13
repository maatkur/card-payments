import sys
from datetime import datetime

from PySide6.QtCore import Signal, QDate
from PySide6.QtWidgets import *

from database.db_handler import DatabaseHandler
from helpers import to_sql_format
from ui.ui_card_management import Ui_Form


class CardManagement(QMainWindow):
    closed = Signal()
    today = datetime.today()
    qdate = QDate(today.year, today.month, today.day)

    def __init__(self) -> None:
        super(CardManagement, self).__init__()
        self.ui = Ui_Form()  # instanciar a classe Ui_form
        self.ui.setupUi(self)
        self.setWindowTitle("Manutenção")
        self.handler = DatabaseHandler()
        self.set_card_flags()
        self.ui.initial_date.setDate(self.qdate)
        self.ui.final_date.setDate(self.qdate)
        self.set_widgets_disable()
        self.ui.order_entry.textChanged.connect(self.verify_entry_text)
        self.ui.nsu_authorization_entry.textChanged.connect(self.verify_entry_text)
        self.ui.by_date_radioButton.clicked.connect(self.check_selected_filter)
        self.ui.by_order_radioButton.clicked.connect(self.check_selected_filter)
        self.ui.by_nsu_authorization_radioButton.clicked.connect(self.check_selected_filter)
        self.ui.tableWidget.cellDoubleClicked.connect(self.set_data_in_edition_fields)
        self.ui.tableWidget.cellDoubleClicked.connect(self.enable_view_widgets)

    def check_selected_filter(self):
        date_radio_checked = self.ui.by_date_radioButton.isChecked()
        order_radio_checked = self.ui.by_order_radioButton.isChecked()
        nsu_authorization_radio_checked = self.ui.by_nsu_authorization_radioButton.isChecked()

        if date_radio_checked:
            self.ui.search_button.setDisabled(False)
            self.ui.initial_date.setDisabled(False)
            self.ui.final_date.setDisabled(False)
            self.ui.search_button.clicked.connect(self.handle_search_button_by_date)
        else:
            self.ui.initial_date.setDisabled(True)
            self.ui.final_date.setDisabled(True)

        if order_radio_checked:
            self.ui.order_entry.setDisabled(False)
            self.ui.search_button.clicked.connect(self.handle_search_button_by_order)
        else:
            self.ui.order_entry.setDisabled(True)
            self.ui.order_entry.setText("")

        if nsu_authorization_radio_checked:
            self.ui.nsu_authorization_entry.setDisabled(False)
            self.ui.search_button.clicked.connect(self.handle_search_button_by_nsu)
        else:
            self.ui.nsu_authorization_entry.setDisabled(True)
            self.ui.nsu_authorization_entry.setText("")

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
                if col == 6:  # verifica se é a coluna da data
                    if isinstance(value, datetime):
                        order_date = value
                    else:
                        order_date = datetime.strptime(value, '%Y-%m-%d')
                    formatted_date = order_date.strftime('%d/%m/%Y')
                    self.ui.tableWidget.setItem(row, col, QTableWidgetItem(formatted_date))
                else:
                    self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(value)))

        self.enable_excel_button()

    def set_card_flags(self) -> None:

        # Busca as bandeiras de cartões no DB e carrega no combobox

        self.handler.connect()
        flags = self.handler.get_card_flags()

        for flag in flags:
            self.ui.flags_comboBox.addItem(flag[0])

        self.handler.disconnect()

    def verify_entry_text(self) -> None:
        is_order_entry_filled = len(self.ui.order_entry.text()) > 0
        is_nsu_entry_filled = len(self.ui.nsu_authorization_entry.text()) > 0

        if is_order_entry_filled or is_nsu_entry_filled:
            self.ui.search_button.setDisabled(False)
        else:
            self.ui.search_button.setDisabled(True)

    def set_widgets_disable(self) -> None:
        self.ui.value_view.setDisabled(True)
        self.ui.nsu_view.setDisabled(True)
        self.ui.order_view.setDisabled(True)
        self.ui.cashier_view.setDisabled(True)
        self.ui.cash_flow_view.setDisabled(True)
        self.ui.authorization_view.setDisabled(True)
        self.ui.transaction_view.setDisabled(True)
        self.ui.flags_comboBox.setDisabled(True)
        self.ui.delete_button.setDisabled(True)
        self.ui.excel_button.setDisabled(True)
        self.ui.save_button.setDisabled(True)
        self.ui.search_button.setDisabled(True)
        self.ui.initial_date.setDisabled(True)
        self.ui.final_date.setDisabled(True)
        self.ui.order_entry.setDisabled(True)
        self.ui.nsu_authorization_entry.setDisabled(True)

    def handle_search_button_by_date(self) -> None:
        initial_date = to_sql_format(self.ui.initial_date.text())
        final_date = to_sql_format(self.ui.final_date.text())

        self.handler.connect()
        data = self.handler.get_orders_by_date_management(initial_date, final_date)
        self.set_data(data)
        self.handler.disconnect()

    def handle_search_button_by_order(self) -> None:
        order = self.ui.order_entry.text()

        self.handler.connect()
        data = self.handler.get_orders_by_number_management(order)
        self.set_data(data)
        self.handler.disconnect()

    def handle_search_button_by_nsu(self) -> None:
        nsu_authorization = self.ui.nsu_authorization_entry.text()

        self.handler.connect()
        data = self.handler.get_orders_by_nsu_or_authorization_management(nsu_authorization)
        self.set_data(data)
        self.handler.disconnect()

    def set_data_in_edition_fields(self, row):
        order = self.ui.tableWidget.item(row, 0).text()
        cashier = self.ui.tableWidget.item(row, 1).text()
        cash_flow = self.ui.tableWidget.item(row, 2).text()
        transaction_type = self.ui.tableWidget.item(row, 3).text()
        flag = self.ui.tableWidget.item(row, 4).text()
        order_value = self.ui.tableWidget.item(row, 5).text()
        nsu = self.ui.tableWidget.item(row, 8).text()
        authorization = self.ui.tableWidget.item(row, 8).text()

        self.ui.order_view.setText(order)
        self.ui.cashier_view.setText(cashier)
        self.ui.cash_flow_view.setText(cash_flow)
        self.ui.transaction_view.setText(transaction_type)
        self.ui.flags_comboBox.setCurrentText(flag)
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
        self.ui.flags_comboBox.setDisabled(False)
        self.ui.delete_button.setDisabled(True)

    def close_details_window(self) -> None:
        self.closed.emit()  # emite o sinal closed quando a janela for fechada
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CardManagement()
    window.show()
    app.exec()
