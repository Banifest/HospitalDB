from PyQt5.QtWidgets import QMessageBox

CODE_STATUS = {
    301: "Не удалось авторизоваться",
    302: "Не удалось создать пациента, введите другой логин",
    303: "Не удалось получить информацию о лекарстве, проверьте введёную информаию",
    304: "Не удалось создать врача, введите другой логин",
    399: "Нет записей по данному запросу",

    200: "Непредвиденная ошибка",
    201: "Не удалось создать пациента с данным логином",
    202: "Не удалось создать пациента с индексом больницы",
    203: "Не удалось создать врача с данным логином",
    204: "Не удалось нанять врача с данными параметрами",
    205: "Не удалось поменять больницу пациенту, проверьте логин и индекс",

    211: "Не удалось просмотреть записи о болезнях",
    212: "Не удалось добавить запись о болезни пациента",
    213: "Не удалось поменять запись о болезне пациента",
    214: "Не удалось назначить лекарство, имя не найденно",
    215: "Не удалось добавить обследование",
    216: "Не удалось просмотреть записи об обследовании",
    217: "Нет данного пациента",
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
