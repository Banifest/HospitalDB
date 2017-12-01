from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class DoctorWindow(QWidget):
    def __init__(self, controller):
        # noinspection PyArgumentList
        super(DoctorWindow, self).__init__()
        self._controller = controller

        uic.loadUi(r'gui\ui\doc_window.ui', self)

        self.see_login_text_box.textChanged.connect(self._controller.set_see_login)

        self.add_login_text_box.textChanged.connect(self._controller.set_add_login)
        self.add_name_disease_text_box.textChanged.connect(self._controller.set_add_name_disease)
        self.add_date_begin_disease.userDateChanged.connect(self._controller.set_add_date_being)
        self.add_is_end_disease.stateChanged.connect(self._controller.set_add_is_end)
        self.add_date_end_disease.userDateChanged.connect(self._controller.set_add_date_end)

        self.change_date_end_disease_text_box.userDateChanged.connect(self._controller.set_change_date_end)

        self.appoint_name_disease_text_box.textChanged.connect(self._controller.set_appoint_name_drag)

        self.see_button.clicked.connect(self._controller.select_disease_patient)
        self.add_disease_button.clicked.connect(self._controller.select_add_disease_patient)
        self.change_button.clicked.connect(self._controller.select_change_disease_patient)
        self.appoint_button.clicked.connect(self._controller.select_add_drag)


        self.show()
