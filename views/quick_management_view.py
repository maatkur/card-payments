import os
import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import Signal

from ui.ui_quick_management import Ui_MainWindow

from database.repositories.repository_manager import RepositoryManager


class QuickManagement(QMainWindow):
    closed = Signal()

    def __init__(self, data) -> None:
        super(QuickManagement, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"Cartões {os.getenv('COMPANY')} | Edição rápida")
        self.data = data
        self.fill_edition_fields()
        self.ui.save_button.clicked.connect(self.handle_save_button)
        self.ui.save_button.clicked.connect(self.close_window)

    def fill_edition_fields(self) -> None:
        self.ui.nsu_edit.setText(self.data["NSU"])
        self.ui.authorization_edit.setText(self.data["transactionAuthorization"])

    def handle_save_button(self) -> None:
        options = {"uId": self.data["uId"],
                   "NSU": self.ui.nsu_edit.text(),
                   "transactionAuthorization": self.ui.authorization_edit.text()
                   }

        if self.data["repository"] == "checkedOrders":
            RepositoryManager.checked_orders_repository().update(options)
        if self.data["repository"] == "oldPayments":
            RepositoryManager.old_payments_repository().update(options)

    def close_window(self) -> None:
        self.deleteLater()
        self.closed.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuickManagement({})
    window.show()
    app.exec()
