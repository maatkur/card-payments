from components.dialog_window import DialogWindow


class DialogWindowManager:
    _dialog = None

    @staticmethod
    def dialog():
        if DialogWindowManager._dialog is None:
            DialogWindowManager._dialog = DialogWindow()
        return DialogWindowManager._dialog
