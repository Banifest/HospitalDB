from PyQt5.QtWidgets import QWidget


class CloseInterface(QWidget):
    def closeEvent(self, QCloseEvent):
        # noinspection PyProtectedMember
        self._controller._mainController.reconnect()
        QCloseEvent.accept()
