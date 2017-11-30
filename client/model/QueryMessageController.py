from PyQt5.QtWidgets import QMessageBox

CODE_STATUS = {
    301: "Не удалось авторизоваться",
    302: "Не удалось создать пользователя введите другой логин",
    303: "Не удалось получить информацию о лекарстве проверьте введёную информаию"
}


class QueryMessageController:
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
