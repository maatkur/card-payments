import sys

from PyQt6.QtWidgets import QMessageBox
from PySide6 import QtCore
from PySide6.QtWidgets import *

from cards import Cards
from ui.ui_cards_login import Ui_MainWindow
from users_list import user_list


class Ui_Login(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(Ui_Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Cartões Obra fácil | Login")
        self.user_entry.installEventFilter(self)
        self.password_entry.installEventFilter(self)
        self.login_button.installEventFilter(self)
        self.login_button.clicked.connect(self.login)
        self.alert = QMessageBox()
        self.users_list = user_list()
        self.card_window = None

    def eventFilter(self, widget, event):
        if event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            if key == QtCore.Qt.Key_Return or key == QtCore.Qt.Key_Enter:
                if widget == self.user_entry:
                    self.focusNextChild()
                if widget == self.password_entry:
                    self.login()

    def login(self):
        user = self.user_entry.text()
        user_code = self.users_list[user]["user_code"]
        password = self.password_entry.text()
        store_unity = self.users_list[user]["store"]
        is_admin_user = self.users_list[user]["admin"]
        auth = (user in self.users_list) and (password == self.users_list[user]["password"])

        if auth:
            window.close()
            if self.card_window is None:
                self.card_window = Cards(is_admin_user, store_unity, user_code)
                self.card_window.show()
        else:
            self.alert.setWindowTitle("Ops!")
            self.alert.setText("Usuário e/ou senha inválido(s)!")
            self.alert.exec()
            self.clear_fields()

    def clear_fields(self):
        self.user_entry.clear()
        self.password_entry.clear()
        self.user_entry.setFocus()
        self.user_name.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_Login()
    window.show()
    app.exec()

