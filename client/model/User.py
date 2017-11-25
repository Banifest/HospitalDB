from datetime import date

from client.model.QueryException import QueryException
from client.model.dbConnect import connection_to_db


class User:
    id: int
    login: str
    password: str
    type: int
    date_registration: date
    fio: str
    birthday: date
    is_auth_success: bool

    def __init__(self, user_id: int = 0, login: str = 0, password: str = 0, user_type: int = 0,
                 date_registration: date = 0, fio: str = 0, birthday: date = 0, is_empty: bool=1):
        if not is_empty:
            self.id = user_id
            self.login = login
            self.password = password
            self.type = user_type
            self.date_registration = date_registration
            self.fio = fio
            self.birthday = birthday

    def set_connection(self, connection):
        self.conn = connection

    def geg_from_db(self, login: str, password: str):
        cursor = self.conn.cursor()

        cursor.execute("EXEC auth_user '{0}', '{1}'".format(login, password))
        row = cursor.fetchone()
        if row is not None:
            self.id = row[0]
            self.type = row[1]
            self.login = row[2]
            self.password = row[3]
            self.date_registration = row[4]
            self.fio = row[5]
        else:
            raise QueryException(301)


    @staticmethod
    def create_user(login: str, password: str, fio: str, gender: bool, zip: str):

        pass