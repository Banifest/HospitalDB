import sys
from PyQt5.QtWidgets import QApplication, QMessageBox

from client.gui.control.AuthController import AuthController
from client.gui.control.RegController import RegController
from client.gui.control.UserController import UserController
from client.model.QueryException import QueryException
from client.model.dbConnect import connection_to_db
from client.model.User import User


# noinspection PyCallByClass
class MainController:
    user: User

    _userController: UserController
    _authController: AuthController
    _regController: RegController

    def __init__(self):
        App = QApplication(sys.argv)
        try:
            self.conn = connection_to_db('test', '123')
            self._authController = AuthController(self, self.conn)
        except QueryException as err:
            MainController.get_error(err)
        App.exec()

    @staticmethod
    def get_error(widget, err):

        pass

    def create_user_window(self, user: User):
        self.user = user
        self._userController = UserController(self, self.user)

    def create_reg_window(self, reg_user: User):
        self._regController = RegController(self, reg_user)
