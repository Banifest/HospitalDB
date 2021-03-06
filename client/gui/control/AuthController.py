from client.gui.view.AuthWindow import AuthWindow
from client.model.User import User


class AuthController:
    login: str = ""
    password: str = ""

    def __init__(self, _mainController, connection):
        self._mainController = _mainController
        self._authWindow = AuthWindow(self)
        self._connection = connection

    def set_connection(self, value):
        self._connection = value

    def set_login(self, login: str):
        self.login = login

    def set_password(self, password: str):
        self.password = password

    def try_auth(self):
        self.user = User()
        self.user.set_connection(self._connection)
        self.user.get(self.login, self.password)

        self.off_enabled()
        if self.user.type == 1:
            self._mainController.create_user_window(self.user)
        elif self.user.type == 2:
            self._mainController.create_reg_window(self.user)
        elif self.user.type == 3:
            self._mainController.create_doctor_window(self.user)
        else:
            self.on_enabled()

    def off_enabled(self):
        self._authWindow.setVisible(False)

    def get_info(self):
        self._mainController.create_info_window()

    def on_enabled(self):
        self._authWindow.setVisible(True)
