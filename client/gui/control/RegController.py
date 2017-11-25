from datetime import date

from client.gui.view.RegWindow import RegWindow
from client.gui.view.UserWindow import UserWindow
from client.model.Patient import Patient
from client.model.User import User


class RegController:
    _regWindow: RegWindow
    _patient: Patient
    gender = True

    def set_login(self, login: str):
        self.login = login

    def set_password(self, password: str):
        self.password = password

    def set_fio(self, fio: str):
        self.fio = fio

    def set_birthday(self, birthday: str):
        self.birthday = birthday

    def set_gender(self, gender: bool):
        self.gender = gender

    def set_zip(self, hospital_zip: bool):
        self.hospital_zip = hospital_zip

    def add_patient(self):
        Patient(connection=self._regUser.conn, fio=self.fio, patient_zip=self.hospital_zip,
                login=self.login, password=self.password, gender=self.gender, birthday=self.birthday).save()

    def __init__(self, _mainController, reg_user: User):
        self._mainController = _mainController
        self._regUser = reg_user
        self._regWindow = RegWindow(self)

