from PySide6.QtWidgets import QMessageBox


class DialogWindow:
    def __init__(self):
        self.message_box = QMessageBox()

    def confirmation(self, title, message):

        self.message_box.setIcon(QMessageBox.Warning)
        self.message_box.setWindowTitle(title)
        self.message_box.setText(message)
        self.message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        self.message_box.setDefaultButton(QMessageBox.Cancel)
        result = self.message_box.exec()

        return result

    def not_found(self):
        title = "Ops!"
        message = "Sem resultados para a busca!"

        self.message_box.setIcon(QMessageBox.Warning)
        self.message_box.setWindowTitle(title)
        self.message_box.setText(message)
        self.message_box.setStandardButtons(QMessageBox.Ok)
        self.message_box.exec()

    def login_error(self):
        title = "Ops!"
        message = "Usuário e/ou senha inválido(s)!"

        self.message_box.setIcon(QMessageBox.Warning)
        self.message_box.setWindowTitle(title)
        self.message_box.setText(message)
        self.message_box.setStandardButtons(QMessageBox.Ok)
        self.message_box.exec()
