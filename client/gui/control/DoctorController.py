from client.gui.view.DoctorWindow import DoctorWindow
from client.model.Doctor import Doctor


class DoctorController:
    _doctor: Doctor
    _id_drag: int = 1
    _name_drag: str = ""
    _get_time_zip: str = ""
    _get_time_fio: str = ""

    def __init__(self, _mainController, doctor: Doctor):
        self._mainController = _mainController
        self._connection = self._mainController.conn
        self._infoWindow = DoctorWindow(self)
        self._doctor = doctor
