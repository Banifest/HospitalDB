from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from client.gui.view.InfoWindow import InfoWindow
from client.model.QueryMessage import QueryMessage
from client.model.QueryThread import QueryThread


class InfoController:
    _id_drag: int = 1
    _name_drag: str = ""
    _get_time_zip: str = ""
    _get_time_fio: str = ""

    HEADERS = {
        'work_time': ["ФИО врача", "Время начала работы", "Время конца работы", "Индекс больницы"],
        'drag': ["Id", "Название лекарства", "Цена", "Срок годности", "Описание", "Масса", "Поставшик",
                 "Надо ли рецепт"]
    }

    def __init__(self, _mainController):
        self._mainController = _mainController
        self._connection = self._mainController.conn
        self._infoWindow = InfoWindow(self)

    @property
    def connection(self):
        return self._connection

    def set_id_drag(self, value):
        self._id_drag = value

    def set_name_drag(self, value):
        self._name_drag = value

    def set_get_time_zip(self, value):
        self._get_time_zip = value

    def set_get_time_fio(self, value):
        self._get_time_fio = value

    def select_time_work_by_zip(self):
        self.standard_out(self.HEADERS['work_time'], "EXEC [get_time_work_by_zip] {0};".format(self._get_time_zip))

    def select_time_work_by_fio(self):
        self.standard_out(self.HEADERS['work_time'], "EXEC [get_time_work_by_fio] '{0}';".format(self._get_time_fio))

    def select_time_work(self):
        self.standard_out(self.HEADERS['work_time'], "EXEC [get_time_work_by_zip_fio] {0}, '{1}';".format(
            self._get_time_zip, self._get_time_fio))

    def select_drag_by_id(self):
        self.standard_out(self.HEADERS['drag'], "EXEC [get_drag_by_id] {0};".format(self._id_drag))

    def select_drag_by_name(self):
        self.standard_out(self.HEADERS['drag'], "EXEC [get_drag_by_name] '{0}';".format(self._name_drag))

    def standard_out(self, header_titles: list, query: str):
        self.thread = QueryThread(query, self.connection)
        self.thread.done.connect(lambda: self.out(header_titles, self.thread.cursor))
        self.thread.start()

    def out(self, header_titles: list, cursor):
        table: QTableWidget = self._infoWindow.table

        table.clearContents()
        table.setColumnCount(len(header_titles))
        table.setHorizontalHeaderLabels(header_titles)
        row = cursor.fetchone()
        table.setRowCount(0)

        if not row:
            QueryMessage(399)
            return
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
