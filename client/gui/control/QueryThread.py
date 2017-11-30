from PyQt5.QtCore import QThread, pyqtSignal


class QueryThread(QThread):
    done = pyqtSignal()
    _query: str = ""
    _connection = None
    cursor = None

    def __init__(self, _query, _connection):
        super().__init__()
        self._query = _query
        self._connection = _connection

    def run(self):
        cursor = self.conn.cursor()
        cursor.execute(self.query)
        self.done.emit()
