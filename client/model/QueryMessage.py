from PyQt5.QtWidgets import QMessageBox

CODE_STATUS = {
    301: "Не удалось авторизоваться",
    302: "Не удалось создать пациента, введите другой логин",
    303: "Не удалось получить информацию о лекарстве, проверьте введёную информаию",
    304: "Не удалось создать врача, введите другой логин",
    399: "Нет записей по данному запросу"
}


class QueryMessage:
    code: int

    def __init__(self, code: int, _window=None):
        super().__init__()
        self.code = code
        # noinspection PyArgumentList
        QMessageBox.warning(_window,
                            CODE_STATUS[code],
                            CODE_STATUS[code],
                            QMessageBox.Ok
                            )
