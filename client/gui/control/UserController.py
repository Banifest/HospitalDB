from client.gui.view.UserWindow import UserWindow
from client.model.Patient import Patient
from client.model.User import User


class UserController:
    _userWindow: UserWindow
    _patient: Patient

    def __init__(self, _mainController, user: User):
        self._mainController = _mainController
        self._patient = Patient(user)

        self._userWindow = UserWindow(self, self._patient)

