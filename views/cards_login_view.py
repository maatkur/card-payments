import os
import sys

from PySide6 import QtCore
from PySide6.QtWidgets import *

from components.dialog_window import DialogWindow
from config.setup_config import setup_config
from ui.ui_cards_login import Ui_MainWindow
from users_list import user_list
from views.cards_view import Cards

setup_config()


class CardsLogin(QMainWindow):
    def __init__(self) -> None:
        super(CardsLogin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"Cartões {os.getenv('COMPANY')} | Login")
        self.install_event_filters()
        self.connect_buttons_actions()
        self.users_list = user_list()
        self.card_window = None
        self.dialog_window = DialogWindow()

    def connect_buttons_actions(self) -> None:
        self.ui.login_button.clicked.connect(self.login)

    def install_event_filters(self) -> None:
        self.ui.user_entry.installEventFilter(self)
        self.ui.password_entry.installEventFilter(self)
        self.ui.login_button.installEventFilter(self)

    def eventFilter(self, widget, event) -> bool:
        if event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            if key == QtCore.Qt.Key_Return or key == QtCore.Qt.Key_Enter:
                if widget == self.ui.user_entry:
                    self.focusNextChild()
                if widget == self.ui.password_entry:
                    self.login()
        return False

    def login(self) -> None:
        user = self.ui.user_entry.text()
        user_code = self.users_list[user]["user_code"]
        password = self.ui.password_entry.text()
        store_unity = self.users_list[user]["store"]
        is_admin_user = self.users_list[user]["admin"]
        auth = (user in self.users_list) and (password == self.users_list[user]["password"])

        if auth:
            window.deleteLater()
            if self.card_window is None:
                self.card_window = Cards(is_admin_user, store_unity, user_code)
                self.card_window.show()
        else:
            self.dialog_window.login_error()
            self.clear_fields()

    def clear_fields(self) -> None:
        self.ui.user_entry.clear()
        self.ui.password_entry.clear()
        self.ui.user_entry.setFocus()
        self.ui.user_name.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CardsLogin()
    window.show()
    app.exec()
