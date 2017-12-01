from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class RegWindow(QWidget):

    def __init__(self, controller):
        self._controller = controller
        # TODO PIVOT
        # noinspection PyArgumentList
        super(RegWindow, self).__init__()
        uic.loadUi(r'gui\ui\reg_window.ui', self)

        self.user_login_text_box.textChanged.connect(self._controller.set_login)
        self.user_password_text_box.textChanged.connect(self._controller.set_password)
        self.user_fio_text_box.textChanged.connect(self._controller.set_fio)
        self.user_birthday.userDateChanged.connect(self._controller.set_birthday)
        self.user_men_radio.clicked.connect(lambda: self._controller.set_gender(True))
        self.user_women_radio.clicked.connect(lambda: self._controller.set_gender(False))
        self.user_zip_text_box.textChanged.connect(self._controller.set_zip)

        self.add_fio_doctor_text_box.textChanged.connect(self._controller.set_add_doctor_fio)
        self.add_login_doctor_text_box.textChanged.connect(self._controller.set_add_doctor_login)
        self.add_password_doctor_text_box.textChanged.connect(self._controller.set_add_doctor_password)
        self.add_date_birthday.userDateChanged.connect(self._controller.set_add_doctor_birthday)
        self.add_discription_doctor_text_box.textChanged.connect(self._controller.set_add_doctor_description)

        self.take_login_doctor_text_box.textChanged.connect(self._controller.set_take_doctor_login)
        self.take_zip_doctor_text_box.textChanged.connect(self._controller.set_take_doctor_zip)
        self.take_special_doctor_text_box.textChanged.connect(self._controller.set_take_doctor_spec)
        self.take_doctor_date_being_work.userDateChanged.connect(self._controller.set_take_doctor_being_date)
        self.take_doctor_time_begin.userTimeChanged.connect(self._controller.set_take_doctor_being_time)
        self.take_doctor_time_end.userTimeChanged.connect(self._controller.set_take_doctor_end_time)

        self.change_login_text_box.textChanged.connect(self._controller.set_change_login)
        self.change_zip_text_box.textChanged.connect(self._controller.set_change_zip)

        self.del_login_text_box.textChanged.connect(self._controller.set_del_login)
        self.del_password_text_box.textChanged.connect(self._controller.set_del_zip)

        self.add_patient_button.clicked.connect(self._controller.add_patient)
        self.create_doctor_button.clicked.connect(self._controller.add_doctor)
        self.take_button.clicked.connect(self._controller.take_doctor)
        self.change_hospital_user_button.clicked.connect(self._controller.change_patient)
        self.del_button.clicked.connect(self._controller.del_doctor)

        self.show()
