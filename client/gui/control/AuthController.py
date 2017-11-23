from client.gui.view.AuthWindow import AuthWindow
from client.model.User import User


class AuthController:
    login: str
    password: str

    def __init__(self, _mainController, connection):
        self._mainController = _mainController
        self._authWindow = AuthWindow(self)
        self._connection = connection

    def set_login(self, login: str):
        self.login = login

    def set_password(self, password: str):
        self.password = password

    def try_auth(self):
        self.user = User(self._connection, self.login, self.password)
        if self.user.type == 1:
            self._mainController.create_user_window(self.user)
