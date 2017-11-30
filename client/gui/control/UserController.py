from datetime import date

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from client.gui.view.UserWindow import UserWindow
from client.model.Patient import Patient
from client.model.User import User


class UserController:
    _userWindow: UserWindow
    _patient: Patient
    _date_begin_disease: date = '01-01-2000'
    _date_end_disease: date = '01-01-2000'
    _id_disease: int = 1

    _date_begin_examination = '01-01-2000'
    _date_end_examination = '01-01-2000'
    _id_examination = 1

    @property
    def login(self):
        return self._patient._user.login

    @property
    def password(self):
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
        self.disease_out("EXEC [get_patient_diseases] '{0}', '{1}', '{2}', '{3}';".format(
            self.login, self.password, self._date_begin_disease, self._date_end_disease))

    def select_exclude_disease(self):
        self.disease_out("EXEC [get_inverse_patient_diseases] '{0}', '{1}', '{2}', '{3}';".format(
            self.login, self.password, self._date_begin_disease, self._date_end_disease))

    def select_list_drags_by_id(self):
        self.drag_out("EXEC [get_drags_by_disease] '{0}', '{1}', {2};".format(
            self.login, self.password, self._id_disease))

    def select_examination(self):
        self.examination_out("EXEC [get_patient_examinations] '{0}', '{1}', '{2}', '{3}'".format(
            self.login, self.password, self._date_begin_examination, self._date_end_examination))

    def select_inverse_examination(self):
        self.examination_out("EXEC [get_inverse_patient_examinations] '{0}', '{1}', '{2}', '{3}'".format(
            self.login, self.password, self._date_begin_examination, self._date_end_examination))

    def select_examination_param(self):
        self.param_examination_out("EXEC get_param_examination '{0}', '{1}', {2}".format(
            self.login, self.password, self._id_examination))

    def select_current_health_state(self):
        self.param_examination_out("EXEC [get_current_state_health] '{0}', '{1}'".format(
            self.login, self.password))

    def disease_out(self, query: str):
        table: QTableWidget = self._userWindow.table
        table.clearContents()
        header_titles = ["Id", "Имя болезни", "Дата начала", "Дата конца"]
        table.setColumnCount(len(header_titles))
        table.setHorizontalHeaderLabels(header_titles)
        cursor = self._patient._user.conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        row_count = 0
        while row:
            table.setItem(row_count, 0, QTableWidgetItem(str(row[0])))
            table.setItem(row_count, 1, QTableWidgetItem(str(row[1])))
            table.setItem(row_count, 2, QTableWidgetItem(str(row[2])))
            table.setItem(row_count, 3, QTableWidgetItem(str(row[3])))
            row_count += 1
            row = cursor.fetchone()

    def drag_out(self, query: str):
        table: QTableWidget = self._userWindow.table
        table.clearContents()
        header_titles = ["Id", "Название лекарства", "Цена", "Срок годности", "Описание", "Масса", "Поставшик", "Надо ли рецепт"]
        table.setColumnCount(len(header_titles))
        table.setHorizontalHeaderLabels(header_titles)
        cursor = self._patient._user.conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        row_count = 0
        while row:
            table.setItem(row_count, 0, QTableWidgetItem(str(row[0])))
            table.setItem(row_count, 1, QTableWidgetItem(str(row[1])))
            table.setItem(row_count, 2, QTableWidgetItem(str(row[2])))
            table.setItem(row_count, 3, QTableWidgetItem(str(row[3])))
            table.setItem(row_count, 4, QTableWidgetItem(str(row[4])))
            table.setItem(row_count, 5, QTableWidgetItem(str(row[5])))
            table.setItem(row_count, 6, QTableWidgetItem(str(row[6])))
            table.setItem(row_count, 7, QTableWidgetItem("Да" if row[7] else "Нет"))
            row_count += 1
            row = cursor.fetchone()

    def examination_out(self, query):
        table: QTableWidget = self._userWindow.table
        table.clearContents()
        header_titles = ["Id", "Название обследования", "Имя врача", "Дата обследования"]
        table.setColumnCount(len(header_titles))
        table.setHorizontalHeaderLabels(header_titles)
        cursor = self._patient._user.conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        row_count = 0
        while row:
            table.setItem(row_count, 0, QTableWidgetItem(str(row[0])))
            table.setItem(row_count, 1, QTableWidgetItem(str(row[1])))
            table.setItem(row_count, 2, QTableWidgetItem(str(row[2])))
            table.setItem(row_count, 3, QTableWidgetItem(str(row[3])))
            row = cursor.fetchone()
            row_count += 1

    def param_examination_out(self, query):
        table: QTableWidget = self._userWindow.table
        table.clearContents()
        header_titles = ["Название характеристики", "Значение характеристики"]
        table.setColumnCount(len(header_titles))
        table.setHorizontalHeaderLabels(header_titles)
        cursor = self._patient._user.conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        row_count = 0
        while row:
            table.setItem(row_count, 0, QTableWidgetItem(str(row[0])))
            table.setItem(row_count, 1, QTableWidgetItem(str(row[1])))
            row = cursor.fetchone()
            row_count += 1
