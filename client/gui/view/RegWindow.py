from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class RegWindow(QWidget):

    def __init__(self, controller):
        self._controller = controller
        # TODO PIVOT
        # noinspection PyArgumentList
        super(RegWindow, self).__init__()
        uic.loadUi(r'gui\ui\reg_window.ui', self)
        self.user_login_text_box.textChanged.connect(self._controller.set_login)
        self.user_password_text_box.textChanged.connect(self._controller.set_password)
        self.user_fio_text_box.textChanged.connect(self._controller.set_fio)
        self.user_birthday.userDateChanged.connect(self._controller.set_birthday)
        self.user_men_radio.clicked.connect(lambda: self._controller.set_gender(True))
        self.user_women_radio.clicked.connect(lambda: self._controller.set_gender(False))
        self.user_zip_text_box.textChanged.connect(self._controller.set_zip)

        self.add_patient_button.clicked.connect(self._controller.add_patient)

        self.show()
