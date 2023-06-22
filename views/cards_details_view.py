import sys

from PySide6.QtCore import Signal
from PySide6.QtWidgets import *

from database.db_handler import DatabaseHandler
from database.repositories.order_stage_repository import OrderStageRepository
from database.repositories.card_flags_repository import CardFlagsRepository
from database.repositories.checked_orders_repository import CheckedOrdersRepository
from database.repositories.stores_repository import StoresRepository
from helpers.date_helpers import to_sql_format, to_default_format
from helpers.paydays_helper import paydays
from ui.ui_cards_details import Ui_Form

from config.setup_config import setup_config

setup_config()


class CardDetails(QMainWindow):
    closed = Signal()

    def __init__(self, order_number, user_type, store) -> None:
        super(CardDetails, self).__init__()
        self.ui = Ui_Form()  # instanciar a classe Ui_form
        self.ui.setupUi(self)
        self.setWindowTitle("Detalhes do cartão")
        self.db_handler = DatabaseHandler()
        self.order_stage_repository = OrderStageRepository()
        self.checked_orders_repository = CheckedOrdersRepository()
        self.card_flags_repository = CardFlagsRepository()
        self.stores_repository = StoresRepository()
        self.order_number = order_number
        self.order_data = self.get_order_data()
        self.clear_fields()
        self.set_order_data()
        self.set_card_flags()
        self.ui.installments_comboBox.setDisabled(True)
        self.ui.save_button.setDisabled(True)
        self.ui.plus_card_button.setDisabled(True)
        self.ui.transaction_type_comboBox.currentIndexChanged.connect(self.allow_installment_combobox_use)
        self.ui.plus_card_button.clicked.connect(self.handle_multiple_card_button)
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

    def get_order_data(self) -> dict:
        options = {
            "distinct": False,
            "query": {
                "orderNumber": self.order_number,
                "isCommit": 0
            }
        }

        order_data = self.order_stage_repository.get_all(options)

        if order_data:
            # Desempacotar os valores da tupla em variáveis
            (
                _,  # Descartar o primeiro elemento (não utilizado)
                order_number,
                cashier_number,
                cash_flow,
                order_value,
                store_unit,
                purchase_date,
                _  # Descartar o último elemento (não utilizado)
            ) = order_data[0]

            # Retornar os valores em um dicionário
            return {
                "orderNumber": order_number,
                "cashierNumber": cashier_number,
                "cashFlow": cash_flow,
                "orderValue": order_value,
                "storeUnit": store_unit,
                "purchaseDate": purchase_date,
            }

    def set_order_data(self) -> None:

        # Carrega as informações do pedido vindas da tabela orderStage

        self.ui.order_label.setText(self.order_data["orderNumber"])
        self.ui.cashier_lineEdit.setText(self.order_data["cashierNumber"])
        self.ui.cash_flow_lineEdit.setText(self.order_data["cashFlow"])

        formatted_value = "{:.2f}".format(round(self.order_data["orderValue"], 2)).replace(".", ",")

        order_date = to_default_format(self.order_data["purchaseDate"])

        self.ui.order_value_lineEdit.setText(str(formatted_value))
        self.ui.sale_date.setText(f"{order_date}")

    def set_card_flags(self) -> None:

        # Busca as bandeiras de cartões no DB e carrega no combobox

        options = {
            "select": "flag",
            "distinct": True,
            "order_by": ["flag"]
        }

        flags = self.card_flags_repository.get_all(options)

        for flag in flags:
            self.ui.card_flag_comboBox.addItem(flag[0])

    def get_card_tax(self, card_flag, installment):
        options = {
            "select": "tax",
            "query": {
                "flag": card_flag,
                "installments": installment,
            }
        }

        return float(self.card_flags_repository.get_all(options)[0][0])

    def allow_installment_combobox_use(self):
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
        self.save_order_details()
        self.close_details_window()

    def create_debit_order(self) -> dict:
        checked_order = {"orderNumber": self.order_number,
                         "cashierNumber": self.order_data["cashierNumber"],
                         "cashFlow": self.order_data["cashFlow"],
                         "transactionType": "debit",
                         "flag": self.ui.card_flag_comboBox.currentText(),
                         "purchaseDate": self.order_data["purchaseDate"],
                         "orderValue": round(float(self.ui.order_value_lineEdit.text().replace(",", ".")), 2),
                         "storeUnit": self.order_data["storeUnit"],
                         "NSU": self.ui.nsu_lineEdit.text(),
                         "transactionAuthorization": self.ui.authorization_lineEdit.text(),
                         "installments": 0,
                         "currentInstallment": 0
                         }

        checked_order["flagTax"] = self.get_card_tax(checked_order["flag"], 0)

        payday = paydays(self.order_data["purchaseDate"], 1, "debit")
        checked_order["payday"] = payday[0]

        liquid_value = round(
            checked_order["orderValue"] - ((checked_order["orderValue"] * checked_order["flagTax"]) / 100), 2)

        checked_order["liquidValue"] = liquid_value
        checked_order["installmentValue"] = liquid_value

        return checked_order

    def create_credit_order(self):
        checked_order = {"orderNumber": self.order_number,
                         "cashierNumber": self.order_data["cashierNumber"],
                         "cashFlow": self.order_data["cashFlow"],
                         "transactionType": 'credit',
                         "flag": self.ui.card_flag_comboBox.currentText(),
                         "purchaseDate": self.order_data["purchaseDate"],
                         "orderValue": round(float(self.ui.order_value_lineEdit.text().replace(",", ".")), 2),
                         "storeUnit": self.order_data["storeUnit"],
                         "NSU": self.ui.nsu_lineEdit.text(),
                         "transactionAuthorization": self.ui.authorization_lineEdit.text(),
                         "installments": int(self.ui.installments_comboBox.currentText()),
                         "currentInstallment": ""
                         }

        checked_order["flagTax"] = self.get_card_tax(checked_order["flag"], checked_order["installments"])

        checked_order["payday"] = paydays(self.order_data["purchaseDate"], checked_order["installments"], "credit")

        liquid_value = round(
            checked_order["orderValue"] - ((checked_order["orderValue"] * checked_order["flagTax"]) / 100), 2)

        checked_order["liquidValue"] = liquid_value
        checked_order["installmentValue"] = liquid_value

        return checked_order

    def save_order_details(self):
        transaction_type = self.ui.transaction_type_comboBox.currentText()
        transaction_type = 'credit' if transaction_type == 'Crédito' else 'debit'

        if transaction_type == "debit":
            checked_order = self.create_debit_order()
            self.checked_orders_repository.insert(checked_order)

        elif transaction_type == 'credit':
            checked_order = self.create_credit_order()

            for installment in range(checked_order["installments"]):
                order_installment = checked_order.copy()
                order_installment["currentInstallment"] = f"{installment + 1}/{order_installment['installments']}"
                order_installment["payday"] = order_installment["payday"][installment]
                self.checked_orders_repository.insert(order_installment)

        self.order_stage_repository.commit_order(self.order_number)

    def process_remaining_payment(self):
        new_value = float(self.ui.order_value_lineEdit.text().replace(",", "."))
        remaining_value = self.initial_value - new_value

        order = {
            "orderNumber": self.order_data["orderNumber"],
            "cashierNumber": str(self.order_data["cashierNumber"]),
            "cashFlow": str(self.order_data["cashFlow"]),
            "orderValue": str(remaining_value),
            "storeUnit": self.stores_repository.get_store_by_id(str(self.store)),
            "isCommit": "0"
        }

        self.order_stage_repository.commit_order(self.order_number)
        self.order_stage_repository.insert(order)

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
            self.close_details_window()

    def handle_multiple_card_button(self):
        self.save_order_details()
        self.process_remaining_payment()
        self.close_details_window()

    def delete_order(self):
        options = {"orderNumber": self.order_number,
                   "isCommit": 0}

        self.order_stage_repository.delete(options)

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
    window = CardDetails("202321", True, 5)
    window.show()
    app.exec()
