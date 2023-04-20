import sys
from datetime import datetime
from PySide6.QtWidgets import *
from PySide6.QtCore import Signal
from ui.ui_cards_details import Ui_Form
from database.db_handler import DatabaseHandler
from paydays import paydays
from helpers import to_sql_format


class CardDetails(QMainWindow):
    closed = Signal()

    def __init__(self, order, user_type, store) -> None:
        super(CardDetails, self).__init__()
        self.ui = Ui_Form()  # instanciar a classe Ui_form
        self.ui.setupUi(self)
        self.setWindowTitle("Detalhes do cartão")
        self.db_handler = DatabaseHandler()
        self.order = order
        self.clear_fields()
        self.set_data()
        self.set_card_flags()
        self.ui.installments_comboBox.setDisabled(True)
        self.ui.save_button.setDisabled(True)
        self.ui.plus_card_button.setDisabled(True)
        self.ui.transaction_type_comboBox.currentIndexChanged.connect(self.allow_installment_comboBox_use)
        self.ui.plus_card_button.clicked.connect(self.handle_plus_card_button)
        self.user_type = user_type
        self.check_user_type()
        self.store = store
        self.initial_value = float(self.ui.order_value_lineEdit.text().replace(",", "."))

        # Dispara os eventos para verificar se o botão de salvar atende os requisitos para ser ativo
        self.ui.card_flag_comboBox.currentIndexChanged.connect(self.active_save_and_plus_button)
        self.ui.transaction_type_comboBox.currentIndexChanged.connect(self.active_save_and_plus_button)
        self.ui.authorization_lineEdit.textChanged.connect(self.active_save_and_plus_button)
        self.ui.nsu_lineEdit.textChanged.connect(self.active_save_and_plus_button)
        self.ui.order_value_lineEdit.textChanged.connect(self.active_save_and_plus_button)

        self.ui.save_button.clicked.connect(self.handle_save_button)
        self.ui.delete_button.clicked.connect(self.handle_delete_button)

    def set_data(self) -> None:

        # Carrega as informações do pedido vindas da tabela orderStage

        self.db_handler.connect()

        order_data = self.db_handler.get_order_details(self.order)

        self.ui.order_label.setText(order_data[0][1])
        self.ui.cashier_lineEdit.setText(order_data[0][2])
        self.ui.cash_flow_lineEdit.setText(order_data[0][3])

        formatted_value = "{:.2f}".format(round(order_data[0][4], 2)).replace(".", ",")

        sale_date_string = order_data[0][6]
        date_object = datetime.strptime(sale_date_string, "%Y-%m-%d")
        formatted_date = date_object.strftime("%d/%m/%Y")

        self.ui.order_value_lineEdit.setText(str(formatted_value))
        self.ui.sale_date.setText(f"{formatted_date}")

        self.db_handler.disconnect()

    def update_data(self, order) -> None:

        # Atualiza um novo pedido sempre que a janela de detalhes é chamada

        self.order = order
        self.set_data()

    def set_card_flags(self) -> None:

        # Busca as bandeiras de cartões no DB e carrega no combobox

        self.db_handler.connect()
        flags = self.db_handler.get_card_flags()

        for flag in flags:
            self.ui.card_flag_comboBox.addItem(flag[0])

        self.db_handler.disconnect()

    def allow_installment_comboBox_use(self):
        is_a_credit_transaction = self.ui.transaction_type_comboBox.currentText() == "Crédito"

        if is_a_credit_transaction:
            self.ui.installments_comboBox.setDisabled(False)
        else:
            self.ui.installments_comboBox.setDisabled(True)
            self.ui.installments_comboBox.setCurrentText('1')

    def active_save_and_plus_button(self) -> None:
        verify_flag_selection = self.ui.card_flag_comboBox.currentText() != "Selecione"
        verify_transaction_type_selection = self.ui.transaction_type_comboBox.currentText() != "Selecione"
        verify_authorization_line_edit = len(self.ui.authorization_lineEdit.text()) > 0
        verify_nsu_line_edit = len(self.ui.nsu_lineEdit.text()) > 0
        verify_order_value = self.initial_value != float(self.ui.order_value_lineEdit.text().replace(",", "."))

        if verify_flag_selection and verify_transaction_type_selection and verify_authorization_line_edit and verify_nsu_line_edit:
            self.ui.save_button.setDisabled(False)
            if verify_order_value:
                self.ui.plus_card_button.setDisabled(False)
            else:
                self.ui.plus_card_button.setDisabled(True)

        else:
            self.ui.save_button.setDisabled(True)
            self.ui.plus_card_button.setDisabled(True)

    def handle_save_button(self) -> None:
        # Salva um pedido com as informações necessárias na tabela 'checkedOrders'

        self.db_handler.connect()

        transaction_type = self.ui.transaction_type_comboBox.currentText()
        transaction_type = 'credit' if transaction_type == 'Crédito' else 'debit'
        flag = self.ui.card_flag_comboBox.currentText()
        installments = int(self.ui.installments_comboBox.currentText())
        order_number = self.order
        nsu = self.ui.nsu_lineEdit.text()
        transaction_authorization = self.ui.authorization_lineEdit.text()
        sale_date = self.ui.sale_date.text().replace("/", "-")
        payday = paydays(sale_date, installments, transaction_type)
        order_value = self.ui.order_value_lineEdit.text().replace(",", ".")

        for installment in range(1, installments + 1):
            current_installment = f"{installment}/{installments}"
            self.db_handler.insert_checked_order(flag, 0 if transaction_type == 'debit' else installments, order_number,
                                                 current_installment,
                                                 payday[installment - 1], order_value,
                                                 nsu, transaction_authorization, transaction_type)

        self.db_handler.update_stage(order_number)
        self.db_handler.disconnect()
        self.close_details_window()

    def handle_delete_button(self):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setWindowTitle("Confirmar exclusão")
        message_box.setText("Tem certeza que deseja excluir?")
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        message_box.setDefaultButton(QMessageBox.Cancel)
        result = message_box.exec_()
        if result == QMessageBox.Yes:
            self.delete_order()

    def handle_plus_card_button(self):

        self.db_handler.connect()

        transaction_type = self.ui.transaction_type_comboBox.currentText()
        transaction_type = 'credit' if transaction_type == 'Crédito' else 'debit'
        flag = self.ui.card_flag_comboBox.currentText()
        installments = int(self.ui.installments_comboBox.currentText())
        order_number = self.order
        nsu = self.ui.nsu_lineEdit.text()
        transaction_authorization = self.ui.authorization_lineEdit.text()
        sale_date = self.ui.sale_date.text().replace("/", "-")
        payday = paydays(sale_date, installments, transaction_type)
        order_value = self.ui.order_value_lineEdit.text().replace(",", ".")
        remaining_value = self.initial_value - float(order_value)
        order_date = to_sql_format(self.ui.sale_date.text())
        cashier_number = self.ui.cashier_lineEdit.text()
        cash_flow = self.ui.cash_flow_lineEdit.text()

        print(f"Restante: {remaining_value}, Inicial: {self.initial_value}")

        for installment in range(1, installments + 1):
            current_installment = f"{installment}/{installments}"
            self.db_handler.insert_checked_order(flag, 0 if transaction_type == 'debit' else installments, order_number,
                                                 current_installment,
                                                 payday[installment - 1], order_value,
                                                 nsu, transaction_authorization, transaction_type)
        self.initial_value = remaining_value
        self.db_handler.update_stage(order_number)
        self.db_handler.manually_insert_in_order_stage(order_number, cashier_number, cash_flow, remaining_value,
                                                       self.store, order_date)
        self.db_handler.disconnect()
        self.close_details_window()

    def delete_order(self):
        self.db_handler.connect()
        self.db_handler.delete_staged_order(self.order)
        self.db_handler.disconnect()
        self.close_details_window()

    def check_user_type(self):
        is_admin_user = self.user_type == "True"

        if is_admin_user:
            self.enable_delete_button()
        else:
            self.disable_delete_button()

    def clear_fields(self) -> None:
        self.ui.nsu_lineEdit.setText("")
        self.ui.authorization_lineEdit.setText("")
        self.ui.installments_comboBox.setCurrentText('1')
        self.ui.card_flag_comboBox.setCurrentText('Selecione')
        self.ui.transaction_type_comboBox.setCurrentText('Selecione')

    def enable_delete_button(self):
        self.ui.delete_button.setDisabled(False)

    def disable_delete_button(self):
        self.ui.delete_button.setDisabled(True)

    def close_details_window(self) -> None:
        self.closed.emit()  # emite o sinal closed quando a janela de detalhes for fechada
        self.clear_fields()
        self.deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CardDetails("")
    window.show()
    app.exec()
