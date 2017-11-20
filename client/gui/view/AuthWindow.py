from PyQt5 import uic
from PyQt5.QtWidgets import QDialog


class AuthWindow(QDialog):

    def __init__(self, controller):
        super(AuthWindow, self).__init__()
        self.controller = controller

        uic.loadUi(r'G:\Новая папка\SQL Server Management Studio\kursach\HospitalDB\client\gui\ui\main_window.ui')

        self.show()
