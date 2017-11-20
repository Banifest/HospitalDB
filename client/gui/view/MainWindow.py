from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, controller):
        super(MainWindow, self).__init__()
        self.controller = controller

        uic.loadUi(r'G:\Новая папка\SQL Server Management Studio\kursach\HospitalDB\client\gui\ui\main_window.ui', self)
        self.auth_button.clicked.connect(self.controller.try_auth)
        self.login_test_box.textChanged.connect(self.controller.set_login)
        self.password_text_box.textChanged.connect(self.controller.set_password)

        self.show()