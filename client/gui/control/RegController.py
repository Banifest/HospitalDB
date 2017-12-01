from client.gui.view.RegWindow import RegWindow
from client.model.Patient import Patient
from client.model.QueryMessage import QueryMessage
from client.model.QueryThread import QueryThread
from client.model.User import User


class RegController:
    _regWindow: RegWindow
    _patient: Patient
    _regUser: User

    @property
    def connection(self):
        return self._regUser.conn

    patient_login: str = ""
    patient_password: str = ""
    patient_fio: str = ""
    patient_birthday: str = "01-01-2000"
    patient_gender: bool = True
    patient_hospital_zip: int = 12345

    add_doctor_fio: str = ""
    add_doctor_login: str = ""
    add_doctor_password: str = ""
    add_doctor_birthday: str = "01-01-2000"
    add_doctor_description: str = ""

    take_doctor_login: str = ""
    take_doctor_zip: str = "12345"
    take_doctor_spec: str = ""
    take_doctor_being_date: str = "01-01-2000"
    take_doctor_being_time: str = "00:00"
    take_doctor_end_time: str = "00:00"

    change_login: str = ""
    change_zip: str = "12345"

    del_login: str = ""
    del_zip: str = "12345"

    def set_del_login(self, value: str):
        self.del_login = value

    def set_del_zip(self, value: str):
        self.del_zip = value

    def set_change_login(self, value: str):
        self.change_login = value

    def set_change_zip(self, value: str):
        self.change_zip = value

    def set_add_doctor_fio(self, value: str):
        self.add_doctor_fio = value

    def set_add_doctor_login(self, value: str):
        self.add_doctor_login = value

    def set_add_doctor_password(self, fio: str):
        self.add_doctor_password = fio

    def set_add_doctor_birthday(self, value):
        self.add_doctor_birthday = value.toString('dd-MM-yyyy')

    def set_add_doctor_description(self, value: str):
        self.add_doctor_description = value

    def set_login(self, value: str):
        self.patient_login = value

    def set_password(self, value: str):
        self.patient_password = value

    def set_fio(self, fio: str):
        self.patient_fio = fio

    def set_birthday(self, value):
        self.patient_birthday = value.toString('dd-MM-yyyy')

    def set_gender(self, value: bool):
        self.patient_gender = value

    def set_zip(self, value: bool):
        self.patient_hospital_zip = value

    def set_take_doctor_being_time(self, value):
        self.take_doctor_being_time = value.toString('HH:mm')

    def set_take_doctor_end_time(self, value):
        self.take_doctor_end_time = value.toString('HH:mm')

    def set_take_doctor_login(self, value: str):
        self.take_doctor_login = value

    def set_take_doctor_zip(self, value: str):
        self.take_doctor_zip = value

    def set_take_doctor_spec(self, value: str):
        self.take_doctor_spec = value

    def set_take_doctor_being_date(self, value):
        self.take_doctor_being_date = value.toString('dd-MM-yyyy')

    def add_patient(self):
        self.get_query("EXEC [add_patient] '{0}', {1}, {2}, '{3}', '{4}', '{5}';"
                       .format(self.patient_fio,
                               self.patient_gender,
                               self.patient_hospital_zip,
                               self.patient_login,
                               self.patient_password,
                               self.patient_birthday))

    def add_doctor(self):
        self.get_query("EXEC [add_doctor] '{0}', {1}, {2}, '{3}', '{4}';"
                       .format(self.add_doctor_fio,
                               self.add_doctor_login,
                               self.add_doctor_password,
                               self.add_doctor_birthday,
                               self.add_doctor_description))

    def take_doctor(self):
        self.get_query("EXEC [take_doctor] '{0}', {1}, {2}, '{3}', '{4}', '{5}';"
                       .format(self.take_doctor_login,
                               self.take_doctor_zip,
                               self.take_doctor_spec,
                               self.take_doctor_being_date,
                               self.take_doctor_being_time,
                               self.take_doctor_end_time))

    def del_doctor(self):
        self.get_query("EXEC [del_doctor] '{0}', {1};"
                       .format(self.del_login,
                               self.del_zip))

    def change_patient(self):
        self.get_query("EXEC [change_patient] '{0}', {1};"
                       .format(self.change_login,
                               self.change_zip))

    def __init__(self, _mainController, reg_user: User):
        self._mainController = _mainController
        self._regUser = reg_user
        self._regWindow = RegWindow(self)

    def get_query(self, query: str):
        self.thread = QueryThread(query, self.connection)
        self.thread.done.connect(lambda: self.out(self.thread.cursor))
        self.thread.start()

    def out(self, cursor):
        row = cursor.fetchone()
        if not row:
            QueryMessage(200)
        elif row[0] != 0:
            QueryMessage(row[0])
        else:
            self.connection.commit()
