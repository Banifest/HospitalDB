from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from client.gui.view.InfoWindow import InfoWindow


class InfoController:
    _id_drag: int = 1
    _name_drag: str = ""
    _get_time_zip: str = ""
    _get_time_fio: str = ""

    def __init__(self, _mainController):
        self._mainController = _mainController
        self._connection = self._mainController.conn
        self._infoWindow = InfoWindow(self)

    def set_id_drag(self, value):
        self._id_drag = value

    def set_name_drag(self, value):
        self._name_drag = value

    def set_get_time_zip(self, value):
        self._get_time_zip = value

    def set_get_time_fio(self, value):
        self._get_time_fio = value

    def select_time_work_by_zip(self):
        pass

    def select_time_work_by_fio(self):
        pass

    def select_time_work(self):
        pass

    def select_drag_by_id(self):
        self.drag_out("EXEC [get_drag_by_id] {0};".format(self._id_drag))

    def select_drag_by_name(self):
        self.drag_out("EXEC [get_drag_by_name] '{0}';".format(self._name_drag))

    def drag_out(self, query: str):
        table: QTableWidget = self._infoWindow.table
        table.clearContents()
        header_titles = [
            "Id", "Название лекарства", "Цена", "Срок годности", "Описание", "Масса", "Поставшик", "Нужен ли рецепт"]
        table.setColumnCount(len(header_titles))
        table.setHorizontalHeaderLabels(header_titles)
        cursor = self._connection.cursor()
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
