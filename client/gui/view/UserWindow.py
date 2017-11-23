from PyQt5 import uic
from PyQt5.QtWidgets import QWidget



class UserWindow(QWidget):

    def __init__(self, controller, patient ):
        self._controller = controller

        super(UserWindow, self).__init__()
        uic.loadUi(r'G:\Новая папка\SQL Server Management Studio\kursach\HospitalDB\client\gui\ui\user_window.ui', self)

        self.fio_label.setText(patient.fio)
        self.birthday_label.setText(patient.birthday)
        self.gender_label.setText(patient.gender)
        self.hospital_label.setText(patient.address)

        self.show()