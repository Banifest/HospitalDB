from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from client.gui.view.DoctorWindow import DoctorWindow
from client.model.Doctor import Doctor
from client.model.QueryMessage import QueryMessage
from client.model.QueryThread import QueryThread


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

    @property
    def cursor(self):
        # noinspection PyProtectedMember
        return self._doctor._user.conn.cursor()

    @property
    def connection(self):
        # noinspection PyProtectedMember
        return self._doctor._user.conn

    @property
    def login(self):
        # noinspection PyProtectedMember
        return self._doctor._user.login

    @property
    def password(self):
        # noinspection PyProtectedMember
        return self._doctor._user.password

    def set_see_login(self, value):
        self._see_login = value

    def set_add_login(self, value):
        self._add_login = value

    def set_add_name_disease(self, value):
        self._add_name_disease = value

    def set_add_date_being(self, value):
        self._add_date_being = value.toString('dd-MM-yyyy')

    def set_add_is_end(self, value):
        self._add_is_end = value
        self._docWindow.add_date_end_disease.setEnabled(value)

    def set_add_date_end(self, value):
        self._add_date_end = value.toString('dd-MM-yyyy')

    def set_change_date_end(self, value):
        self._change_date_end = value.toString('dd-MM-yyyy')

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
        self._docWindow = DoctorWindow(self)
        self._doctor = doctor

    def out(self, header_titles: list, cursor, table: QTableWidget = None):
        if not table:
            table: QTableWidget = self._docWindow.table

        table.clearContents()
        table.setColumnCount(len(header_titles))
        table.setHorizontalHeaderLabels(header_titles)
        row = cursor.fetchone()
        if not row:
            QueryMessage(399)
            return

        row_count = 0
        table.setRowCount(row_count)
        while row:
            table.setRowCount(row_count + 1)
            for x in range(len(header_titles)):
                if str(row[x]) == 'True' or str(row[x]) == 'False':
                    table.setItem(row_count, x, QTableWidgetItem("Да" if row[7] else "Нет"))
                else:
                    table.setItem(row_count, x, QTableWidgetItem(str(row[x])))
            row_count += 1
            row = cursor.fetchone()

        table.resizeColumnsToContents()

    def standard_out(self, header_titles: list, query: str):
        self.thread = QueryThread(query, self.connection)
        self.thread.done.connect(lambda: self.out(header_titles, self.thread.cursor))
        self.thread.start()

    def additional_out(self, header_titles: list, query: str):
        self.thread = QueryThread(query, self.connection)
        self.thread.done.connect(lambda: self.out(header_titles, self.thread.cursor, table=self._docWindow.desc_table))
        self.thread.start()

    def change_additional(self, row_number: int, columb_number: int):
        if self.currentState == self.SELECT_STATE['examination']:
            pass  # self.select_examination_param(int(self._docWindow.table.item(row_number, 0).text()))
        elif self.currentState == self.SELECT_STATE['disease']:
            pass  # self.select_list_drags_by_id(int(self._docWindow.table.item(row_number, 0).text()))
