use [test]
GO
GRANT EXECUTE ON [dbo].[auth_user] TO [authorization] WITH GRANT OPTION 
GO
GRANT EXECUTE ON [dbo].[get_drag_by_id] TO [authorization] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_drag_by_name] TO [authorization] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_time_work_by_fio] TO [authorization] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_time_work_by_zip] TO [authorization] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_time_work_by_zip_fio] TO [authorization] WITH GRANT OPTION
GO
-------------------------
use [test]
GO
GRANT EXECUTE ON [dbo].[get_inverse_patient_diseases] TO [patient] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_inverse_patient_examinations] TO [patient] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_current_state_health] TO [patient] WITH GRANT OPTION
GO
REVOKE GRANT OPTION FOR EXECUTE ON [dbo].[get_current_state_health] TO [patient] CASCADE AS [dbo]
GO
GRANT EXECUTE ON [dbo].[get_patient] TO [patient] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_patient_examinations] TO [patient] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_param_examination] TO [patient] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_drags_by_disease] TO [patient] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_patient_diseases] TO [patient] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[auth_user] TO [patient] WITH GRANT OPTION
------------------------------------
use [test]
GO
GRANT EXECUTE ON [dbo].[add_doctor] TO [registrator] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[add_patient] TO [registrator] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[auth_user] TO [registrator] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[change_patient] TO [registrator] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[del_doctor] TO [registrator] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[EXPORT_HOSPITALS] TO [registrator] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[IMPORT_HOSPITALS] TO [registrator] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[take_doctor] TO [registrator] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_patient_diseases] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_exclude_doctor_examinations] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[select_users] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[see_exm_doc] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_statistic_by_index_year] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_patient] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[auth_user] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[appoint_drag] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_param_examination] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_patient_examinations] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_statistic_by_index] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_statistic_by_year] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[select_disease] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[add_param] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[change_disease] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_statistic_by_all_time] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[add_disease] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[add_examination] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_doctor_examinations] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_doctor_examination_param] TO [doctor] WITH GRANT OPTION
GO
GRANT EXECUTE ON [dbo].[get_drags_by_disease_doctor] TO [doctor] WITH GRANT OPTION
