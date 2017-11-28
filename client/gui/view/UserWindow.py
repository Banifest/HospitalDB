from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QTableView


class UserWindow(QWidget):

    def __init__(self, controller, patient):
        self._controller = controller

        super(UserWindow, self).__init__()
        uic.loadUi(r'G:\Новая папка\SQL Server Management Studio\kursach\HospitalDB\client\gui\ui\user_window.ui', self)

        self.fio_label.setText(patient.fio)
        self.birthday_label.setText(patient.birthday)
        self.gender_label.setText(patient.gender)
        self.hospital_label.setText(patient.zip)

        self.date_begining_disease.userDateChanged.connect(self._controller.set_date_begin_disease)
        self.date_ending_disease.userDateChanged.connect(self._controller.set_date_end_disease)
        self.disease_id_text_box.textChanged.connect(self._controller.set_id_disease)
        self.drag_id_text_box.textChanged.connect(self._controller.set_id_drag)
        self.drag_name_text_box.textChanged.connect(self._controller.set_name_drag)

        self.include_disease_button.clicked.connect(self._controller.select_include_disease)
        self.exclude_disease_button.clicked.connect(self._controller.select_exclude_disease)
        self.list_drags_disease_button.clicked.connect(self._controller.select_list_drags_by_id)
        self.drag_by_id_button.clicked.connect(self._controller.select_drag_by_id)
        self.drag_by_name_button.clicked.connect(self._controller.select_drag_by_name)

        self.show()
