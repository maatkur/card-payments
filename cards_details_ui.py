from PySide6.QtWidgets import *
from PySide6.QtCore import Signal, QTimer
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
        self.ui.installments_comboBox.setDisabled(True)
        self.ui.save_button.clicked.connect(self.insert_checked_order)
        self.ui.transaction_type_comboBox.currentIndexChanged.connect(self.allow_installment_comboBox_use)

    def set_data(self) -> None:

        # Carrega as informações do pedido vindas da tabela orderStage

        self.db_handler.connect()

        order_data = self.db_handler.get_order(self.order)

        self.ui.order_label.setText(order_data[0][1])
        self.ui.cashier_lineEdit.setText(order_data[0][2])
        self.ui.cash_flow_lineEdit.setText(order_data[0][3])

        formatted_value = "{:.2f}".format(round(order_data[0][4], 2)).replace(".", ",")

        sale_date_string = order_data[0][6].strftime('%d/%m/%Y')

        self.ui.order_value_lineEdit.setText(str(formatted_value))
        self.ui.sale_date.setText(f"{sale_date_string}")

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

    def insert_checked_order(self) -> None:
        print("Inserting checked order...")
        # Salva um pedido com as informações necessárias na tabela 'checkedOrders'

        self.db_handler.connect()

        transaction_type = self.ui.transaction_type_comboBox.currentText()
        transaction_type = 'credit' if transaction_type == 'Crédito' else 'debit'
        flag = self.ui.card_flag_comboBox.currentText()
        installments = self.ui.installments_comboBox.currentText()
        order_number = self.order
        nsu = self.ui.nsu_lineEdit.text()
        transaction_authorization = self.ui.authorization_lineEdit.text()
        sale_date = self.ui.sale_date.text().replace("/", "-")
        payday = paydays(sale_date, installments, transaction_type)

        for installment in range(1, int(installments) + 1):
            current_installment = f"{installment}/{installments}"
            print(f"Inserting installment {current_installment}")
            self.db_handler.insert_order(flag, installments, order_number, current_installment, payday[installment - 1],
                                         nsu, transaction_authorization, transaction_type)

        self.db_handler.update_stage(order_number)
        self.db_handler.disconnect()
        self.closed.emit()
        QTimer.singleShot(500, self.close_details_window)

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
