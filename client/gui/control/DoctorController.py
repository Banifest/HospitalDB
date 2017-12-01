from client.gui.view.DoctorWindow import DoctorWindow
from client.model.Doctor import Doctor


class DoctorController:
    currentState = 0
    SELECT_STATE: dict = {
        'none': 0,
        'disease': 1,
        'drag': 2,
        'examination': 3
    }

    _doctor: Doctor
    _id_drag: int = 1
    _name_drag: str = ""
    _get_time_zip: str = ""
    _get_time_fio: str = ""

    _add_login: str = ""
    _add_name_disease: str = ""
    _add_date_being: str = "01-01-2000"
    _add_is_end: bool = True
    _add_date_end: str = "01-01-2000"

    _change_login: str = ""
    _change_id_disease: int = 1
    _change_date_end: str = ""

    _see_login: str = ""

    _appoint_id_disease: int = 1
    _appoint_name_drag: str = ""

    def set_see_login(self, value):
        self._see_login = value

    def set_add_login(self, value):
        self._add_login = value

    def set_add_name_disease(self, value):
        self._add_name_disease = value

    def set_add_date_being(self, value):
        self._add_date_being = value

    def set_add_is_end(self, value):
        self._add_is_end = value

    def set_add_date_end(self, value):
        self._add_date_end = value

    def set_change_date_end(self, value):
        self._change_date_end = value

    def set_appoint_name_drag(self, value):
        self._appoint_name_drag = value

    def select_disease_patient(self):
        pass

    def select_add_disease_patient(self):
        pass

    def select_change_disease_patient(self):
        pass

    def select_add_drag(self):
        pass

    def __init__(self, _mainController, doctor: Doctor):
        self._mainController = _mainController
        self._connection = self._mainController.conn
        self._infoWindow = DoctorWindow(self)
        self._doctor = doctor
