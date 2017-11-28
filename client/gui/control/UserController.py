from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from datetime import date

from client.gui.view.UserWindow import UserWindow
from client.model.Patient import Patient
from client.model.User import User


class UserController:
    _userWindow: UserWindow
    _patient: Patient
    _date_begin_disease: date = '01-01-2000'
    _date_end_disease: date = '01-01-2000'
    _id_disease: int = 1
    _id_drag: int = 1
    _name_drag: str = ""

    def __init__(self, _mainController, user: User):
        self._mainController = _mainController
        self._patient = Patient()
        self._patient.get(user.conn, login=user.login, password=user.password)

        self._userWindow = UserWindow(self, self._patient)

    def set_date_begin_disease(self, value: date):
        self._date_begin_disease = value.toString('dd-MM-yyyy')

    def set_date_end_disease(self, value: date):
        self._date_end_disease = value.toString('dd-MM-yyyy')

    def set_id_disease(self, value: str):
        self._id_disease = value

    def set_id_drag(self, value):
        self._id_drag = value

    def set_name_drag(self, value):
        self._name_drag = value

    def select_include_disease(self):
        self.disease_out("EXEC [get_patient_diseases] '{0}', '{1}', '{2}', '{3}';".format(
            self._patient._user.login, self._patient._user.password, self._date_begin_disease, self._date_end_disease))

    def select_exclude_disease(self):
        self.disease_out("EXEC [get_inverse_patient_diseases] '{0}', '{1}', '{2}', '{3}';".format(
            self._patient._user.login, self._patient._user.password, self._date_begin_disease, self._date_end_disease))

    def select_list_drags_by_id(self):
        self.drag_out("EXEC [get_drags_by_disease] '{0}', '{1}', {2};".format(
            self._patient._user.login, self._patient._user.password, self._id_disease))

    def select_drag_by_id(self):
        self.drag_out("EXEC [get_drag_by_id] {0};".format(self._id_drag))

    def select_drag_by_name(self):
        self.drag_out("EXEC [get_drag_by_name] '{0}';".format(self._name_drag))

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
        table.setHorizontalHeaderLabels(header_titles)
        table.setColumnCount(len(header_titles))
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