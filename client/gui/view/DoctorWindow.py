from PyQt5 import uic

from client.gui.view.CloseInterface import CloseInterface


class DoctorWindow(CloseInterface):
    def __init__(self, controller):
        # noinspection PyArgumentList
        super(DoctorWindow, self).__init__()
        self._controller = controller

        uic.loadUi(r'gui\ui\doc_window.ui', self)

        self.see_login_text_box.textChanged.connect(self._controller.set_see_login)

        self.add_login_text_box.textChanged.connect(self._controller.set_add_login)
        self.add_name_disease_text_box.textChanged.connect(self._controller.set_add_name_disease)
        self.add_date_begin_disease.userDateChanged.connect(self._controller.set_add_date_being)
        self.add_is_end_disease.stateChanged.connect(self._controller.set_add_is_end)
        self.add_date_end_disease.userDateChanged.connect(self._controller.set_add_date_end)
        self.add_desc_disease_text_box.textChanged.connect(self._controller.set_add_decs_disease)

        self.change_date_end_disease_text_box.userDateChanged.connect(self._controller.set_change_date_end)

        self.appoint_name_disease_text_box.textChanged.connect(self._controller.set_appoint_name_drag)

        self.see_exm_login_text_box.textChanged.connect(self._controller.set_see_exm_login)
        self.see_exm_date_begin.userDateChanged.connect(self._controller.set_see_exm_date_begin)
        self.see_exm_date_end.userDateChanged.connect(self._controller.set_see_exm_date_end)

        self.add_exm_login_text_box.textChanged.connect(self._controller.set_emx_login)
        self.add_exm_name_text_box.textChanged.connect(self._controller.set_emx_name)
        self.add_exm_date.userDateChanged.connect(self._controller.set_exm_date)

        self.add_param_name_text_box.textChanged.connect(self._controller.set_param_name)
        self.add_param_val_text_box.textChanged.connect(self._controller.set_param_val)

        self.get_stat_index_text_box.valueChanged.connect(self._controller.set_get_stat_index)
        self.get_stat_date.userDateChanged.connect(self._controller.set_get_stat_date)

        self.see_button.clicked.connect(self._controller.select_disease_patient)
        self.add_disease_button.clicked.connect(self._controller.select_add_disease_patient)
        self.change_button.clicked.connect(self._controller.select_change_disease_patient)
        self.appoint_button.clicked.connect(self._controller.select_add_drag)
        self.add_exm_button.clicked.connect(self._controller.select_add_emx)
        self.add_param_button.clicked.connect(self._controller.select_add_param)
        self.see_exm_button.clicked.connect(self._controller.select_see_emx)
        self.see_exclude_exm_button.clicked.connect(self._controller.select_see_exclude_emx)
        self.get_stat_by_all_time.clicked.connect(self._controller.select_stat_by_all_time)
        self.get_stat_by_index.clicked.connect(self._controller.select_stat_by_index)
        self.get_stat_by_year.clicked.connect(self._controller.select_stat_by_year)
        self.get_stat_by_index_year.clicked.connect(self._controller.select_stat_by_index_yearh)

        self.table.cellClicked.connect(lambda a, b: self._controller.change_additional(a, b))

        self.show()
