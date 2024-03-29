from PySide6.QtWidgets import QLineEdit, QTableWidget, QPushButton, QDateEdit
from PySide6.QtCore import QDate
from datetime import datetime


class WidgetHelpers:

    @staticmethod
    def connect_texts_changes(window, method):
        lineedits = window.findChildren(QLineEdit)  # Obtém todos os line edits da tela
        for lineedit in lineedits:
            lineedit.textChanged.connect(method)

    @staticmethod
    def line_edits_filled(window):
        lineedits = window.findChildren(QLineEdit)  # Obtém todos os line edits da tela
        for lineedit in lineedits:
            if lineedit.text().strip() == '':
                return False  # Se um line edit estiver vazio, retorna False
        return True  # Todos os line edits estão preenchidos

    @staticmethod
    def manage_buttons(window, set_disabled: bool):
        buttons = window.findChildren(QPushButton)  # Obtém todos os line edits da tela
        for button in buttons:
            button.setDisabled(set_disabled)

    @staticmethod
    def clear_table(window):
        tables_widgets = window.findChildren(QTableWidget)

        for table in tables_widgets:
            table.clearContents()
            table.setRowCount(0)

    @staticmethod
    def set_current_date(window):
        date_widgets = window.findChildren(QDateEdit)
        today = datetime.today()
        qdate = QDate(today.year, today.month, today.day)

        for date_edit in date_widgets:
            date_edit.setDate(qdate)