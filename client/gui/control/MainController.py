import sys

from PyQt5.QtWidgets import QApplication

from client.gui.control.AuthController import AuthController
from client.gui.control.DoctorController import DoctorController
from client.gui.control.InfoController import InfoController
from client.gui.control.RegController import RegController
from client.gui.control.UserController import UserController
from client.model.Doctor import Doctor
from client.model.User import User
from client.model.dbConnect import connection_to_db


# noinspection PyCallByClass
class MainController:
    user: User

    _userController: UserController
    _authController: AuthController
    _regController: RegController
    _doctorController: DoctorController

    def __init__(self):
        App = QApplication(sys.argv)
        self.conn = connection_to_db('test', '123')
        #        self.conn = connection_to_db(username='reg', password='reg')
        self._authController = AuthController(self, self.conn)
        App.exec()

    def create_user_window(self, user: User):
        self.user = user
        self._userController = UserController(self, self.user)

    def create_reg_window(self, reg_user: User):
        # reg_user.conn.close()
        # reg_user.conn = connection_to_db(username='reg', password='reg')
        reg_user.conn.autocommit(False)
        self._regController = RegController(self, reg_user)

    def create_info_window(self):
        self._infoController = InfoController(self)

    def create_doctor_window(self, doctor_user: User):
        self._doctorController = DoctorController(self, Doctor(user=doctor_user))

    def reconnect(self):
        self.conn.close()
        self.conn = connection_to_db('test', '123')
        self._authController.set_connection(self.conn)
        self._authController.on_enabled()
