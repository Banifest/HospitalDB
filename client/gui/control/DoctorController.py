from PyQt5.QtCore import QDate
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
        'examination': 3,
        'stat': 4
    }

    HEADERS = {
        'stat': ["Имя заболевания", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
                 "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"],

        'param': ["Имя заболеввания", "Название параметра", "Значение параметра"],

        'examination': ["Id", "Дата обследования", "Название обследования", ],

        'disease': ["Id", "Имя заболевания", "Дата начала", "Дата конца", "Описание болезни"],

        'drag': ["Id", "Название лекарства", "Цена", "Срок годности", "Описание", "Масса", "Поставшик",
                 "Надо ли рецепт"]
    }

    selected_row = -1
    selected_column = -1
    selected_id = -1

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
    _add_decs_disease: str = ""

    _change_login: str = ""
    _change_id_disease: int = 1
    _change_date_end: str = "01-01-2000"

    _see_login: str = ""

    _see_exm_login: str = ""
    _see_exm_date_begin: str = "01-01-2000"
    _see_exm_date_end: str = "01-01-2000"

    _appoint_id_disease: int = 1
    _appoint_name_drag: str = ""

    _exm_login: str = ""
    _exm_name: str = ""
    _exm_date: str = '01-01-2000'

    _param_name: str = ""
    _param_val: str = ""

    _get_stat_date: str = "01-01-2000"
    _get_stat_index: int = "220000"

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

    def set_see_exm_login(self, value):
        self._see_exm_login = value

    def set_emx_login(self, value):
        self._exm_login = value

    def set_emx_name(self, value):
        self._exm_name = value

    def set_param_name(self, value):
        self._param_name = value

    def set_param_val(self, value):
        self._param_val = value

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

    def set_add_decs_disease(self, value):
        self._add_decs_disease = value

    def set_add_date_end(self, value):
        self._add_date_end = value.toString('dd-MM-yyyy')

    def set_change_date_end(self, value):
        self._change_date_end = value.toString('dd-MM-yyyy')

    def set_appoint_name_drag(self, value):
        self._appoint_name_drag = value

    def set_see_exm_date_begin(self, value):
        self._see_exm_date_begin = value.toString('dd-MM-yyyy')

    def set_see_exm_date_end(self, value):
        self._see_exm_date_end = value.toString('dd-MM-yyyy')

    def set_exm_date(self, value):
        self._exm_date = value.toString('dd-MM-yyyy')

    def set_get_stat_index(self, value):
        self._get_stat_index = value

    def set_get_stat_date(self, value):
        self._get_stat_date = value.toString('dd-MM-yyyy')

    def select_disease_patient(self):
        self.currentState = self.SELECT_STATE['disease']
        self.standard_out(self.HEADERS['disease'],
                          "EXEC select_disease '{0}', '{1}', '{2}'".format(
                              self._see_login, self.login, self.password))

    def select_add_disease_patient(self):
        self._docWindow.see_login_text_box.setText(self._add_login)
        self.standard_out(self.HEADERS['disease'],
                          "EXEC add_disease '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}'".format(
                              self._add_login, self.login, self.password, self._add_name_disease,
                              self._add_date_being, self._add_date_end, self._add_decs_disease),
                          callback=self.select_disease_patient)
        self.currentState = self.SELECT_STATE['disease']

    def select_change_disease_patient(self):
        if self.currentState == self.SELECT_STATE['disease'] and self.selected_row != -1:
            self.standard_out(self.HEADERS['disease'],
                              "EXEC [change_disease] {0}, '{1}'".format(
                                  self.selected_id, self._change_date_end),
                              callback=self.select_disease_patient)

    def select_add_drag(self):
        if self.currentState == self.SELECT_STATE['disease'] and self.selected_row != -1:
            self.additional_out(self.HEADERS['drag'],
                                "EXEC [appoint_drag] {0}, '{1}'".format(
                                    self.selected_id, self._appoint_name_drag),
                                callback=self.select_drag)

    def select_add_emx(self):
        self._docWindow.see_exm_login_text_box.setText(self._exm_login)
        self._docWindow.see_exm_date_begin.setDate(QDate(1800, 1, 1))
        self._docWindow.see_exm_date_end.setDate(QDate(3000, 1, 1))
        self.standard_out(self.HEADERS['examination'],
                          "EXEC [add_examination] '{0}', '{1}', '{2}', '{3}', '{4}'".format(
                              self.login, self.password, self._exm_login, self._exm_name, self._exm_date),
                          callback=self.select_see_emx)

    def select_add_param(self):
        if self.currentState == self.SELECT_STATE['examination'] and self.selected_row != -1:
            self.standard_out(self.HEADERS['disease'],
                              "EXEC [add_param] '{0}', '{1}', '{2}', '{3}', '{4}'".format(
                                  self.selected_id, self.login, self.password, self._param_name, self._param_val),
                              callback=self.select_get_param)
        else:
            QueryMessage(300)

    def select_get_param(self):
        self.additional_out(self.HEADERS['param'],
                            "EXEC [get_doctor_examination_param] '{0}', '{1}', {2}".format(
                                self.login, self.password, self.selected_id
                            ))

    def select_see_emx(self):
        self.currentState = self.SELECT_STATE['examination']
        self.standard_out(self.HEADERS['examination'],
                          "EXEC [get_doctor_examinations] '{0}', '{1}', '{2}', '{3}', '{4}'".format(
                              self._see_exm_login, self.login, self.password, self._see_exm_date_begin,
                              self._see_exm_date_end
                          ))

    def select_see_exclude_emx(self):
        self.currentState = self.SELECT_STATE['examination']
        self.standard_out(self.HEADERS['examination'],
                          "EXEC [get_exclude_doctor_examinations] '{0}', '{1}', '{2}', '{3}', '{4}'".format(
                              self._see_exm_login, self.login, self.password, self._see_exm_date_begin,
                              self._see_exm_date_end
                          ))

    def select_drag(self):
        self.additional_out(self.HEADERS['drag'],
                            "EXEC [get_drags_by_disease_doctor] '{0}', '{1}', {2};".format(
            self.login, self.password, int(self._docWindow.table.item(self.selected_row, 0).text())))

    def select_stat_by_all_time(self):
        self.currentState = self.SELECT_STATE['stat']
        self.standard_out(self.HEADERS['stat'],
                          "EXEC get_statistic_by_all_time")

    def select_stat_by_index(self):
        self.currentState = self.SELECT_STATE['stat']
        self.standard_out(self.HEADERS['stat'],
                          "EXEC get_statistic_by_index {0}".format(
                              self._get_stat_index
                          ))

    def select_stat_by_year(self):
        self.currentState = self.SELECT_STATE['stat']
        self.standard_out(self.HEADERS['stat'],
                          "EXEC get_statistic_by_year '{0}'".format(
                              self._get_stat_date
                          ))

    def select_stat_by_index_year(self):
        self.currentState = self.SELECT_STATE['stat']
        self.standard_out(self.HEADERS['stat'],
                          "EXEC get_statistic_by_index_year {0}, '{1}'".format(
                              self._get_stat_index, self._get_stat_date
                          ))

    def __init__(self, _mainController, doctor: Doctor):
        self._mainController = _mainController
        self._connection = self._mainController.conn
        self._docWindow = DoctorWindow(self)
        self._doctor = doctor

    def out(self, header_titles: list, cursor, table: QTableWidget = None, callback=None):
        if not table:
            table: QTableWidget = self._docWindow.table

        table.clearContents()
        table.setColumnCount(len(header_titles))
        table.setHorizontalHeaderLabels(header_titles)
        row = cursor.fetchone()
        table.setRowCount(0)
        table.resizeColumnsToContents()

        if not row:
            QueryMessage(399)
            return
        elif row[0] == 0 and callback is not None:
            callback()
        elif len(row) == 1:
            QueryMessage(row[0])
        else:
            row_count = 0
            while row:
                table.setRowCount(row_count + 1)
                for x in range(len(header_titles)):
                    if str(row[x]) == 'True' or str(row[x]) == 'False':
                        table.setItem(row_count, x, QTableWidgetItem("Да" if row[7] else "Нет"))
                    elif str(row[x]) == 'None':
                        table.setItem(row_count, x, QTableWidgetItem("-"))
                    else:
                        table.setItem(row_count, x, QTableWidgetItem(str(row[x])))
                row_count += 1
                row = cursor.fetchone()

            table.resizeColumnsToContents()

            if table == self._docWindow.table:
                self.selected_row = -1
                self.selected_column = -1
                self._docWindow.desc_table.clearContents()
                self._docWindow.desc_table.setRowCount(0)

    def standard_out(self, header_titles: list, query: str, callback=None):
        self.thread = QueryThread(query, self.connection)
        self.thread.done.connect(lambda: self.out(header_titles, self.thread.cursor, callback=callback))
        self.thread.start()

    def additional_out(self, header_titles: list, query: str, callback=None):
        self.thread = QueryThread(query, self.connection)
        self.thread.done.connect(lambda: self.out(header_titles, self.thread.cursor, table=self._docWindow.desc_table,
                                                  callback=callback))
        self.thread.start()

    def change_additional(self, row_number: int, column_number: int):
        self.selected_row = row_number
        self.selected_column = column_number
        self.selected_id = int(self._docWindow.table.item(row_number, 0).text())
        if self.currentState == self.SELECT_STATE['examination']:
            self.select_get_param()
        elif self.currentState == self.SELECT_STATE['disease']:
            self.select_drag()
