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

    def __init__(self, connection, login: str, password: str):
        self.conn = connection
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
