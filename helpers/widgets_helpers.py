from PySide6.QtWidgets import QLineEdit


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
