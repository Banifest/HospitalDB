from datetime import date

from client.gui.view.RegWindow import RegWindow
from client.model.Patient import Patient
from client.model.User import User


class RegController:
    _regWindow: RegWindow
    _patient: Patient
    gender = True
    birthday: date = '01-01-2000'

    def set_login(self, value: str):
        self.login = value

    def set_password(self, value: str):
        self.password = value

    def set_fio(self, fio: str):
        self.fio = fio

    def set_birthday(self, value):
        self.birthday = value.toString('dd-MM-yyyy')

    def set_gender(self, value: bool):
        self.gender = value

    def set_zip(self, value: bool):
        self.hospital_zip = value

    def add_patient(self):
        Patient(connection=self._regUser.conn, fio=self.fio, patient_zip=self.hospital_zip,
                login=self.login, password=self.password, gender=self.gender, birthday=self.birthday).save()

    def __init__(self, _mainController, reg_user: User):
        self._mainController = _mainController
        self._regUser = reg_user
        self._regWindow = RegWindow(self)

