import sys

from PySide6.QtCore import Signal
from PySide6.QtWidgets import *

from database.repositories.repository_manager import RepositoryManager
from helpers.date_helpers import DateHelpers
from helpers.uuid_helpers import UuidHelpers
from helpers.order_helpers import OrderHelpers
from ui.ui_cards_details import Ui_Form
from components.dialog_window import DialogWindow


class CardDetails(QMainWindow):
    closed = Signal()

    def __init__(self, order_uid, is_admin_user, store) -> None:
        super(CardDetails, self).__init__()
        self.ui = Ui_Form()  # instanciar a classe Ui_form
        self.ui.setupUi(self)
        self.setWindowTitle("Detalhes do cartão")
        self.dialog_window = DialogWindow()
        self.order_uid = order_uid
        self.order_data = None
        self.fetch_and_load_data()
        self.initial_value = float(self.ui.order_value_lineEdit.text().replace(",", "."))
        self.set_card_flags()
        self.disable_installments_combo_box()
        self.disable_save_button()
        self.disable_multiple_card_button()
        self.connect_buttons_actions()
        self.connect_widgets_actions()
        self.is_admin_user = is_admin_user
        self.check_user_type()
        self.store = store

    def connect_widgets_actions(self):
        self.ui.card_flag_comboBox.currentIndexChanged.connect(self.active_save_and_plus_button)
        self.ui.transaction_type_comboBox.currentIndexChanged.connect(self.active_save_and_plus_button)
        self.ui.authorization_lineEdit.textChanged.connect(self.active_save_and_plus_button)
        self.ui.nsu_lineEdit.textChanged.connect(self.active_save_and_plus_button)
        self.ui.order_value_lineEdit.textChanged.connect(self.active_save_and_plus_button)
        self.ui.transaction_type_comboBox.currentIndexChanged.connect(self.allow_installment_combobox_use)

    def connect_buttons_actions(self):
        self.ui.save_button.clicked.connect(self.handle_save_button)
        self.ui.delete_button.clicked.connect(self.handle_delete_button)
        self.ui.plus_card_button.clicked.connect(self.handle_multiple_card_button)

    def fetch_order_data(self) -> None:
        self.order_data = RepositoryManager.order_stage_repository().get_order_to_check(self.order_uid)

    def load_order_data(self) -> None:

        # Carrega as informações do pedido vindas da tabela orderStage

        self.ui.order_label.setText(self.order_data["orderNumber"])
        self.ui.cashier_lineEdit.setText(self.order_data["cashierNumber"])
        self.ui.cash_flow_lineEdit.setText(self.order_data["cashFlow"])

        formatted_value = "{:.2f}".format(round(self.order_data["orderValue"], 2)).replace(".", ",")

        order_date = DateHelpers.to_default_format(self.order_data["purchaseDate"])

        self.ui.order_value_lineEdit.setText(str(formatted_value))
        self.ui.sale_date.setText(f"{order_date}")

    def fetch_and_load_data(self):
        self.fetch_order_data()
        self.load_order_data()

    def set_card_flags(self) -> None:

        # Busca as bandeiras de cartões no DB e carrega no combobox

        options = {
            "select": "flag",
            "distinct": True,
            "order_by": ["flag"]
        }

        flags = RepositoryManager.card_flags_repository().get_all(options)

        for flag in flags:
            self.ui.card_flag_comboBox.addItem(flag[0])

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
            self.enable_save_button()
            if verify_order_value:
                self.enable_multiple_card_button()
            else:
                self.disable_multiple_card_button()

        else:
            self.disable_save_button()
            self.disable_multiple_card_button()

    def handle_save_button(self) -> None:
        self.create_and_save_order()
        self.close_details_window()

    def create_and_save_order(self) -> None:
        transaction_type = self.ui.transaction_type_comboBox.currentText()

        order = self.order_data
        order["nsu"] = self.ui.nsu_lineEdit.text()
        order["transactionAuthorization"] = self.ui.authorization_lineEdit.text()
        order["orderValue"] = self.ui.order_value_lineEdit.text().replace(",", ".")
        order["flag"] = self.ui.card_flag_comboBox.currentText()
        order["installments"] = self.ui.installments_comboBox.currentText()
        order["transactionType"] = transaction_type

        checked_order = OrderHelpers.create_checked_order(order)

        if type(checked_order) == dict:
            RepositoryManager.checked_orders_repository().insert_debit_order(checked_order)
        else:
            RepositoryManager.checked_orders_repository().inser_credit_order(checked_order)

        self.update_order_stage()

    def process_remaining_payment(self):
        new_value = float(self.ui.order_value_lineEdit.text().replace(",", "."))
        remaining_value = self.initial_value - new_value
        print(remaining_value)
        order = {
            "orderNumber": self.order_data["orderNumber"],
            "cashierNumber": str(self.order_data["cashierNumber"]),
            "cashFlow": str(self.order_data["cashFlow"]),
            "dateUpdate": self.order_data["purchaseDate"],
            "orderValue": str(remaining_value),
            "storeUnit": RepositoryManager.stores_repository().get_store_by_id(str(self.store)),
            "isCommit": "0",
            "uId": UuidHelpers.generate_uuid()
        }

        self.update_order_stage()
        RepositoryManager.order_stage_repository().insert(order)

    def update_order_stage(self) -> None:
        order_uid = self.order_data["uId"]
        new_value = float(self.ui.order_value_lineEdit.text().replace(",", "."))

        RepositoryManager.order_stage_repository().update_order_value(new_value, order_uid)
        RepositoryManager.order_stage_repository().commit_order(order_uid)

    def handle_delete_button(self):

        window_tittle = "Confirmar exclusão"
        window_message = "Tem certeza que deseja excluir?"

        result = self.dialog_window.confirmation(window_tittle, window_message)
        if result == QMessageBox.Yes:
            self.delete_order()
            self.close_details_window()

    def handle_multiple_card_button(self):
        self.create_and_save_order()
        self.process_remaining_payment()
        self.close_details_window()

    def delete_order(self):
        options = {"uId": self.order_data["uId"],
                   "isCommit": 0}

        RepositoryManager.order_stage_repository().delete(options)

    def check_user_type(self):

        if self.is_admin_user:
            self.enable_delete_button()
        else:
            self.disable_delete_button()

    def enable_delete_button(self):
        self.ui.delete_button.setDisabled(False)

    def disable_delete_button(self):
        self.ui.delete_button.setDisabled(True)

    def enable_installments_combo_box(self):
        self.ui.installments_comboBox.setDisabled(False)

    def disable_installments_combo_box(self):
        self.ui.installments_comboBox.setDisabled(True)

    def enable_save_button(self):
        self.ui.save_button.setDisabled(False)

    def disable_save_button(self):
        self.ui.save_button.setDisabled(True)

    def enable_multiple_card_button(self):
        self.ui.plus_card_button.setDisabled(False)

    def disable_multiple_card_button(self):
        self.ui.plus_card_button.setDisabled(True)

    def close_details_window(self) -> None:
        self.closed.emit()  # emite o sinal closed quando a janela de detalhes for fechada
        self.deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CardDetails("202321", True, 5)
    window.show()
    app.exec()
