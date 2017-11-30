import sys

from PyQt5.QtWidgets import QApplication

from client.gui.control.AuthController import AuthController
from client.gui.control.InfoController import InfoController
from client.gui.control.RegController import RegController
from client.gui.control.UserController import UserController
from client.model.User import User
from client.model.dbConnect import connection_to_db


# noinspection PyCallByClass
class MainController:
    user: User

    _userController: UserController
    _authController: AuthController
    _regController: RegController

    def __init__(self):
        App = QApplication(sys.argv)
        self.conn = connection_to_db('test', '123')
        self._authController = AuthController(self, self.conn)
        App.exec()

    @staticmethod
    def get_error(widget, err):
        pass

    def create_user_window(self, user: User):
        self.user = user
        self._userController = UserController(self, self.user)

    def create_reg_window(self, reg_user: User):
        self._regController = RegController(self, reg_user)

    def create_info_window(self):
        self._infoController = InfoController(self)
