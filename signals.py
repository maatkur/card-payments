from PySide6.QtCore import QObject, Signal
from db_handler import DatabaseHandler


class Signals(QObject):
    card_details_closed = Signal(str)

    def __init__(self, flag, installments, order_number, NSU, transactionAuthorization):
        super().__init__()
        self.db_handler = DatabaseHandler()
        self.flag = flag
        self.installments = installments
        self.order_number = order_number
        self.nsu = NSU
        self.transaction_authorization = transactionAuthorization

    def run(self):
        self.db_handler.connect()
        self.db_handler.insert_checked_orders(self.flag, self.installments, self.order_number, self.nsu,
                                              self.transaction_authorization)
        self.card_details_closed.emit()
