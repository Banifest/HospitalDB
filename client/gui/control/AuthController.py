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
        self.user = User()
        self.user.set_connection(self._connection)
        self.user.geg_from_db(self.login, self.password)
        if self.user.type == 1:
            self._mainController.create_user_window(self.user)
        elif self.user.type == 2:
            self._mainController.create_reg_window(self.user)

