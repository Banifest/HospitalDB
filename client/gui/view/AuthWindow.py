from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class AuthWindow(QMainWindow):
    def __init__(self, controller):
        super(AuthWindow, self).__init__()
        self._controller = controller

        uic.loadUi(r'G:\Новая папка\SQL Server Management Studio\kursach\HospitalDB\client\gui\ui\auth_window.ui', self)
        self.auth_button.clicked.connect(self._controller.try_auth)
        self.login_test_box.textChanged.connect(self._controller.set_login)
        self.password_text_box.textChanged.connect(self._controller.set_password)

        self.show()