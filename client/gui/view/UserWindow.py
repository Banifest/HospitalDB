from PyQt5 import uic

from client.gui.view.CloseInterface import CloseInterface


class UserWindow(CloseInterface):

    def __init__(self, controller, patient):
        self._controller = controller

        # noinspection PyArgumentList
        super(UserWindow, self).__init__()
        uic.loadUi(r'gui\ui\user_window.ui', self)

        self.fio_label.setText(patient.fio)
        self.birthday_label.setText(patient.birthday)
        self.gender_label.setText(patient.gender)
        self.hospital_label.setText(patient.zip)

        self.date_begining_disease.userDateChanged.connect(self._controller.set_date_begin_disease)
        self.date_ending_disease.userDateChanged.connect(self._controller.set_date_end_disease)

        self.include_disease_button.clicked.connect(self._controller.select_include_disease)
        self.exclude_disease_button.clicked.connect(self._controller.select_exclude_disease)

        # Section 3
        self.date_begin_examinations.userDateChanged.connect(self._controller.set_date_begin_examination)
        self.date_end_examinations.userDateChanged.connect(self._controller.set_date_end_examination)
        self.include_examination_button.clicked.connect(self._controller.select_examination)
        self.exclude_examination_button.clicked.connect(self._controller.select_inverse_examination)

        self.current_state_health_button.clicked.connect(self._controller.select_current_health_state)

        self.table.cellClicked.connect(lambda a, b: self._controller.change_additional(a))

        self.show()