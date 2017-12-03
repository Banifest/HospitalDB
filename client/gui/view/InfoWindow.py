from PyQt5 import uic

from client.gui.view.CloseInterface import CloseInterface


class InfoWindow(CloseInterface):
    def __init__(self, controller):
        # noinspection PyArgumentList
        super(InfoWindow, self).__init__()
        self._controller = controller

        uic.loadUi(r'gui\ui\info_window.ui', self)

        # get info drag section
        self.drag_id_text_box.textChanged.connect(self._controller.set_id_drag)
        self.drag_name_text_box.textChanged.connect(self._controller.set_name_drag)

        self.drag_by_id_button.clicked.connect(self._controller.select_drag_by_id)
        self.drag_by_name_button.clicked.connect(self._controller.select_drag_by_name)

        # get info time work section
        self.get_work_time_zip_text_box.textChanged.connect(self._controller.set_get_time_zip)
        self.get_work_time_fio_text_box.textChanged.connect(self._controller.set_get_time_fio)
        self.get_time_work_by_zip_button.clicked.connect(self._controller.select_time_work_by_zip)
        self.get_time_work_by_fio_button.clicked.connect(self._controller.select_time_work_by_fio)
        self.get_time_work_button.clicked.connect(self._controller.select_time_work)

        self.show()
