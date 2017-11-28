from datetime import date

from client.model.QueryException import QueryException
from client.model.User import User


class Patient:
    _user: User
    _gender: bool
    _hospitalAddress: str

    @property
    def gender(self) -> str:
        return 'мужской' if self._gender else 'женский'

    @property
    def fio(self) -> str:
        return self._user.fio

    @property
    def birthday(self) -> str:
        return str(self._user.birthday)

    @property
    def zip(self) -> int:
        return self._hospitalAddress

    def __init__(self, user: User=None, login: str = 0, password: str = 0, user_type: int = 0, fio: str = 0,
                 birthday: str = "", patient_zip: int=None, connection=None, gender: bool=None):
        if user is not None:
            self._user = user
        else:
            self._user = User(fio=fio, birthday=birthday, login=login, password=password, user_type=user_type, is_empty=False)
            self._user.set_connection(connection)
        self._hospitalZip = patient_zip
        self._gender = gender

    def get(self, conn, login, password):
        self._user = User(connection=conn)
        self._user.get(login, password)
        cursor = self._user.conn.cursor()
        cursor.execute("EXEC get_patient '{0}', '{1}'".format(self._user.login, self._user.password))
        row = cursor.fetchone()
        if row is not None:
            self._user.fio = row[0]
            self._user.birthday = row[1]
            self._gender = row[2]
            self._hospitalAddress = row[3]

    def save(self):
        cursor = self._user.conn.cursor()
        cursor.execute("EXEC add_patient '{0}', {1}, {2}, '{3}', '{4}', '{5}';"
                       .format(self.fio, self._gender, self.zip, self._user.login, self._user.password,
                               self.birthday))
        print("EXEC add_patient '{0}', {1}, {2}, '{3}', '{4}', '{5}';"
                       .format(self.fio, self._gender, self.zip, self._user.login, self._user.password,
                               self.birthday))
        try:
            row = cursor.fetchone()
        except: pass
        else: raise QueryException(202)
