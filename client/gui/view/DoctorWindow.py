from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class DoctorWindow(QWidget):
    def __init__(self, controller):
        # noinspection PyArgumentList
        super(DoctorWindow, self).__init__()
        self._controller = controller

        uic.loadUi(r'G:\Новая папка\SQL Server Management Studio\kursach\HospitalDB\client\gui\ui\doc_window.ui', self)

        self.show()
