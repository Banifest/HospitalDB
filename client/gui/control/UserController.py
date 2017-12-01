from datetime import date

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from client.gui.view.UserWindow import UserWindow
from client.model.Patient import Patient
from client.model.QueryMessage import QueryMessage
from client.model.QueryThread import QueryThread
from client.model.User import User


class UserController:
    currentState = 0
    SELECT_STATE: dict = {
        'none': 0,
        'disease': 1,
        'drag': 2,
        'examination': 3
    }

    _userWindow: UserWindow
    _patient: Patient
    _date_begin_disease: date = '01-01-2000'
    _date_end_disease: date = '01-01-2000'
    _id_disease: int = 1

    _date_begin_examination = '01-01-2000'
    _date_end_examination = '01-01-2000'
    _id_examination = 1

    PARAM_HEADER = ["Название характеристики", "Значение характеристики"]
    DISEASE_HEADER = ["Id", "Имя болезни", "Дата начала", "Дата конца"]
    DRAG_HEADER = ["Id", "Название лекарства", "Цена", "Срок годности", "Описание", "Масса", "Поставшик",
                   "Надо ли рецепт"]
    EXAMINATION_HEADER = ["Id", "Название обследования", "Имя врача", "Дата обследования"]

    @property
    def cursor(self):
        # noinspection PyProtectedMember
        return self._patient._user.conn.cursor()

    @property
    def connection(self):
        # noinspection PyProtectedMember
        return self._patient._user.conn

    @property
    def login(self):
        # noinspection PyProtectedMember
        return self._patient._user.login

    @property
    def password(self):
        # noinspection PyProtectedMember
        return self._patient._user.password

    def __init__(self, _mainController, user: User):
        self._mainController = _mainController
        self._patient = Patient()
        self._patient.get(user.conn, login=user.login, password=user.password)

        self._userWindow = UserWindow(self, self._patient)

    def set_date_begin_disease(self, value: date):
        self._date_begin_disease = value.toString('dd-MM-yyyy')

    def set_date_end_disease(self, value: date):
        self._date_end_disease = value.toString('dd-MM-yyyy')

    def set_date_begin_examination(self, value: date):
        self._date_begin_examination = value.toString('dd-MM-yyyy')

    def set_date_end_examination(self, value: date):
        self._date_end_examination = value.toString('dd-MM-yyyy')

    def set_id_disease(self, value: str):
        self._id_disease = value

    def set_id_examination(self, value):
        self._id_examination = value

    def select_include_disease(self):
        self.currentState = self.SELECT_STATE['disease']
        self.standard_out(self.DISEASE_HEADER, "EXEC [get_patient_diseases] '{0}', '{1}', '{2}', '{3}';"
                          .format(self.login, self.password, self._date_begin_disease, self._date_end_disease))

    def select_exclude_disease(self):
        self.currentState = self.SELECT_STATE['disease']
        self.standard_out(self.DISEASE_HEADER, "EXEC [get_inverse_patient_diseases] '{0}', '{1}', '{2}', '{3}';"
                          .format(self.login, self.password, self._date_begin_disease, self._date_end_disease))

    def select_list_drags_by_id(self, id_):
        self.additional_out(self.DRAG_HEADER, "EXEC [get_drags_by_disease] '{0}', '{1}', {2};".format(
            self.login, self.password, id_))

    def select_examination(self):
        self.currentState = self.SELECT_STATE['examination']
        self.standard_out(self.EXAMINATION_HEADER, "EXEC [get_patient_examinations] '{0}', '{1}', '{2}', '{3}'".format(
            self.login, self.password, self._date_begin_examination, self._date_end_examination))

    def select_inverse_examination(self):
        self.currentState = self.SELECT_STATE['examination']
        self.standard_out(self.EXAMINATION_HEADER,
                          "EXEC [get_inverse_patient_examinations] '{0}', '{1}', '{2}', '{3}'".format(
                              self.login, self.password, self._date_begin_examination, self._date_end_examination))

    def select_examination_param(self, id_):
        self.additional_out(self.PARAM_HEADER, "EXEC get_param_examination '{0}', '{1}', {2}".format(
            self.login, self.password, id_))

    def select_current_health_state(self):
        self.currentState = self.SELECT_STATE['none']
        self.standard_out(self.PARAM_HEADER, "EXEC [get_current_state_health] '{0}', '{1}'".format(
            self.login, self.password))

    def out(self, header_titles: list, cursor, table: QTableWidget = None):
        if not table:
            table: QTableWidget = self._userWindow.table

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
        self.thread.done.connect(lambda: self.out(header_titles, self.thread.cursor, table=self._userWindow.desc_table))
        self.thread.start()

    def change_additional(self, row_number: int):
        if self.currentState == self.SELECT_STATE['examination']:
            self.select_examination_param(int(self._userWindow.table.item(row_number, 0).text()))
        elif self.currentState == self.SELECT_STATE['disease']:
            self.select_list_drags_by_id(int(self._userWindow.table.item(row_number, 0).text()))
