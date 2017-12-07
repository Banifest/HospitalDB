CREATE INDEX nick_password_index
    ON dbo.Users
    (nick, password)
GO
CREATE INDEX nick__index
    ON dbo.Users
    (nick)
GO
CREATE INDEX patien_id_disease_index
ON dbo.Diseases (patient_id)
GO
CREATE INDEX patien_id_examination_index
ON dbo.Diseases (patient_id)
GO
CREATE INDEX user_id_patient_index
ON dbo.Patients (user_id)
GO
CREATE INDEX user_id_doctor_index
ON dbo.Doctors(user_id)
GO
CREATE INDEX zip_index
ON dbo.Hospitals(zip)
GO
CREATE INDEX drag_name_index
ON dbo.Drags(name)
GO
CREATE INDEX date_begin_end_index
ON dbo.Diseases(begin_date, end_date)
GO
CREATE INDEX check_date_index
ON dbo.Examinations(check_date)
GO
CREATE INDEX DoctorsHospitals_index
ON dbo.DoctorsHospitals(doctor_id, hospital_id)