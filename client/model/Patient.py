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
    def address(self) -> str:
        return self._hospitalAddress

    def __init__(self, user: User):
        self._user = user

        cursor = self._user.conn.cursor()
        cursor.execute("EXEC get_patient '{0}', '{1}'".format(self._user.login, self._user.password))
        row = cursor.fetchone()
        if row is not None:
            self._user.fio = row[0]
            self._user.birthday = row[1]
            self._gender = row[2]
            self._hospitalAddress = row[3]
