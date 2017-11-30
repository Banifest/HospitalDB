from client.gui.view.DoctorWindow import DoctorWindow


class DoctorController:
    _id_drag: int = 1
    _name_drag: str = ""
    _get_time_zip: str = ""
    _get_time_fio: str = ""

    def __init__(self, _mainController):
        self._mainController = _mainController
        self._connection = self._mainController.conn
        self._infoWindow = DoctorWindow(self)
