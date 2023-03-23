from PySide6.QtWidgets import *
from PySide6.QtCore import Signal
import sys
from ui_cards_details import Ui_Form
from db_handler import DatabaseHandler
from paydays import paydays


class CardDetails(QMainWindow):
    closed = Signal()

    def __init__(self, order) -> None:
        super(CardDetails, self).__init__()
        self.ui = Ui_Form()  # instanciar a classe Ui_form
        self.ui.setupUi(self)
        self.setWindowTitle("Detalhes do cartão")
        self.db_handler = DatabaseHandler()
        self.order = order
        self.set_data()
        self.set_card_flags()
        self.ui.save_button.clicked.connect(self.insert_checked_order)

    def set_data(self) -> None:

        # Carrega as informações do pedido vindas da tabela orderStage

        self.db_handler.connect()

        order_data = self.db_handler.get_order(self.order)

        transaction_type = order_data[0][4]

        self.check_transaction_type(transaction_type)

        self.ui.order_label.setText(order_data[0][1])
        self.ui.cashier_lineEdit.setText(order_data[0][2])
        self.ui.cash_flow_lineEdit.setText(order_data[0][3])

        formatted_value = "{:.2f}".format(round(order_data[0][5], 2)).replace(".", ",")

        sale_date_string = order_data[0][7].strftime('%d/%m/%Y')

        self.ui.order_value_lineEdit.setText(str(formatted_value))
        self.ui.sale_date.setText(f"{sale_date_string}")

        self.db_handler.disconnect()

    def check_transaction_type(self, transaction_type) -> None:

        if transaction_type == 'credit':
            transaction_type = 'Crédito'
            self.ui.installments_comboBox.setDisabled(False)
            self.ui.transaction_type_mask.setText('credit')
            self.ui.transaction_type_lineEdit.setText(transaction_type)
        elif transaction_type == 'debit':
            transaction_type = 'Débito'
            self.ui.installments_comboBox.setDisabled(True)
            self.ui.transaction_type_mask.setText('debit')
            self.ui.transaction_type_lineEdit.setText(transaction_type)


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

    def insert_checked_order(self) -> None:

        # Salva um pedido com as informações necessárias na tabela 'checkedOrders'

        self.db_handler.connect()

        flag = self.ui.card_flag_comboBox.currentText()
        installments = self.ui.installments_comboBox.currentText()
        order_number = self.order
        nsu = self.ui.nsu_lineEdit.text()
        transaction_authorization = self.ui.authorization_lineEdit.text()
        transaction_type = self.ui.transaction_type_mask.text()
        sale_date = self.ui.sale_date.text().replace("/", "-")
        payday = paydays(sale_date, installments, transaction_type)

        for installment in range(1, int(installments)+1):
            current_installment = f"{installment}/{installments}"
            self.db_handler.insert_purchase(flag, installments, order_number, current_installment, payday[installment - 1], nsu, transaction_authorization)

        self.db_handler.update_stage(order_number)
        self.db_handler.disconnect()
        self.closed.emit()
        self.close_details_window()

    def clear_fields(self) -> None:
        self.ui.nsu_lineEdit.setText("")
        self.ui.authorization_lineEdit.setText("")
        self.ui.installments_comboBox.setCurrentText('1')

    def close_details_window(self) -> None:
        self.closed.emit()  # emite o sinal closed quando a janela de detalhes for fechada
        self.clear_fields()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CardDetails("202321")
    window.show()
    app.exec()