import sys
from PyQt5.QtWidgets import QApplication

from client.gui.view.AuthWindow import AuthWindow
from client.gui.view.MainWindow import MainWindow
from client.model.dbConnect import connection_to_db
from client.model.user_action import User


class MainController:
    user: User
    login: str
    password: str

    def __init__(self):
        App = QApplication(sys.argv)
        self.conn = connection_to_db('test','123')
        self._mainWindow = MainWindow(self)
        App.exec()

    def set_login(self, login: str):
        self.login = login

    def set_password(self, login: str):
        self.password = login

    def try_auth(self):
        self.user = User(self.conn, self.login, self.password)
