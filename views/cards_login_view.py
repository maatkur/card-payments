import os
import sys

from PySide6 import QtCore
from PySide6.QtWidgets import *

from components.dialog_window import DialogWindow
from database.repositories.repository_manager import RepositoryManager
from config.setup_config import setup_config
from ui.ui_cards_login import Ui_MainWindow
from views.cards_view import Cards
from helpers.widgets_helpers import WidgetHelpers


setup_config()


class CardsLogin(QMainWindow):
    def __init__(self) -> None:
        super(CardsLogin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"Cartões {os.getenv('COMPANY')} | Login")
        self.install_event_filters()
        self.connect_buttons_actions()
        self.connect_texts_chages()

        self.card_window = None
        self.dialog_window = DialogWindow()

    def connect_buttons_actions(self) -> None:
        self.ui.login_button.clicked.connect(self.authenticate_user)

    def connect_texts_chages(self) -> None:
        WidgetHelpers.connect_texts_changes(self, self.enable_login_button)

    def install_event_filters(self) -> None:
        self.ui.user_entry.installEventFilter(self)
        self.ui.password_entry.installEventFilter(self)
        self.ui.login_button.installEventFilter(self)

    def eventFilter(self, widget, event) -> bool:
        if event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            if key == QtCore.Qt.Key_Return or key == QtCore.Qt.Key_Enter:
                if widget == self.ui.user_entry and self.id_entry_filled():
                    self.focusNextChild()
                if widget == self.ui.password_entry and self.password_entry_filled():
                    self.authenticate_user()
        return False

    def authenticate_user(self) -> None:
        incomming_code = self.ui.user_entry.text()
        incomming_password = self.ui.password_entry.text()

        authentication = RepositoryManager.users_repository().authenticate_user(incomming_code, incomming_password)

        if authentication:
            window.deleteLater()
            logged_user = RepositoryManager.users_repository().get_user_info(incomming_code)
            if self.card_window is None:
                self.card_window = Cards(logged_user)
                self.card_window.show()
        else:
            self.dialog_window.login_error()
            self.clear_fields()

    def clear_fields(self) -> None:
        self.ui.user_entry.clear()
        self.ui.password_entry.clear()
        self.ui.user_entry.setFocus()
        self.ui.user_name.setText("")

    def manage_login_button(self) -> None:

        if self.id_entry_filled and self.password_entry_filled:
            self.enable_login_button()
        else:
            self.disable_login_button()

    def enable_login_button(self) -> None:
        self.ui.login_button.setDisabled(False)

    def disable_login_button(self) -> None:
        self.ui.login_button.setDisabled(True)

    def id_entry_filled(self) -> bool:
        id_entry_filled = len(self.ui.user_entry.text()) > 0

        return id_entry_filled

    def password_entry_filled(self) -> bool:
        id_entry_filled = len(self.ui.password_entry.text()) > 0

        return id_entry_filled


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CardsLogin()
    window.show()
    app.exec()
