USE test
GO
CREATE PROCEDURE dbo.add_patient 
    @fio nvarchar(50),
	@gender bit,
	@hospital_id int,
	@nick nvarchar(50), 
	@password nvarchar(50),
	@birthday date 
AS
BEGIN TRAN
	DECLARE @check_nick int;
	SELECT @check_nick = count(*) FROM Users WHERE nick = @nick;
	if(@check_nick = 0)
		INSERT INTO Users
		(
			type,
			nick,
			password,
			date_registration,
			fio,
			birthday
		)
		values
		(
			1,
			@nick,
			@password,
			SYSDATETIME(),
			@fio,
			@birthday
		)
	else
		ROLLBACK

	DECLARE @user_id int;
	SELECT @user_id = id FROM Users WHERE nick = @nick;
	INSERT INTO Patients
	(
		gender,
		hospital_id,
		user_id
	)
	VALUES
	(
		@gender,
		@hospital_id,
		@user_id
	)
COMMIT TRAN

GO
CREATE PROCEDURE dbo.add_doctor 
    @fio nvarchar(50),
	@hospital_id int,
	@nick nvarchar(50), 
	@password nvarchar(50),
	@date_begin_working date,
	@speciality nvarchar(50),
	@birthday date
AS
BEGIN TRAN
	DECLARE @check_nick int;
	SELECT @check_nick = count(*) FROM Users WHERE nick = @nick;
	if(@check_nick = 0)
		INSERT INTO Users
		(
			type,
			nick,
			password,
			date_registration,
			fio,
			birthday
		)
		values
		(
			1,
			@nick,
			@password,
			SYSDATETIME(),
			@fio,
			@birthday
		)
	else
		ROLLBACK

	DECLARE @user_id int;
	SELECT @user_id = id FROM Users WHERE nick = @nick;
	INSERT INTO Doctors
	(
		user_id
	)
	VALUES
	(
		@user_id
	)

	DECLARE @doctor_id int;
	SELECT @doctor_id = id FROM Doctors WHERE user_id = @user_id;

	INSERT INTO DoctorsHospitals
	(
		date_begin_working,
		doctor_id,
		hospital_id,
		speciality
	)
	VALUES
	(
		@date_begin_working,
		@doctor_id,
		@hospital_id,
		@speciality
	)
COMMIT TRAN
GO
	CREATE PROCEDURE dbo.add_hospital 
    @address nvarchar(50),
	@zip int,
	@phone nvarchar(15), 
	@main_doctor int
AS
BEGIN TRAN
	INSERT INTO hospital.dbo.Hospitals
	(
		address,
		zip,
		phone,
		main_doctor
	)
	values
	(
		@address,
		@zip,
		@phone,
		@main_doctor
	)
COMMIT TRAN
GO
	CREATE PROCEDURE dbo.add_examination 
    @doctor_id int,
	@patient_id int,
	@param xml
AS
BEGIN TRAN
	INSERT INTO hospital.dbo.Examinations
	(
		doctor_id,
		patient_id,
		param
	)
	values
	(
		@doctor_id,
		@patient_id,
		@param
	)
COMMIT TRAN
GO
	CREATE PROCEDURE dbo.add_disease 
    @name_disease nvarchar(50),
	@begin_date date,
	@end_date date,
	@doctor_id int,
	@patient_id int
AS
BEGIN TRAN
	INSERT INTO hospital.dbo.Diseases
	(
		name_disease,
		begin_date,
		end_date,
		doctor_id,
		patient_id
	)
	values
	(
		@doctor_id,
		@begin_date,
		@end_date,
		@doctor_id,
		@patient_id
	)
COMMIT TRAN
GO
	CREATE PROCEDURE dbo.add_drags_to_disease 
    @disease_id int,
	@drag_id int
AS
BEGIN TRAN
	INSERT INTO hospital.dbo.DiseasesDrags
	(
		disease_id,
		drag_id
	)
	values
	(
		@disease_id,
		@drag_id
	)
COMMIT TRAN
GO
CREATE PROCEDURE dbo.add_user
	  @fio nvarchar(50),
	  @nick nvarchar(50),
	  @password nvarchar(50),
	  @birthday date
AS
BEGIN TRANSACTION
  DECLARE @check_nick int;
	SELECT @check_nick = count(*) FROM Users WHERE nick = @nick;
	if(@check_nick = 0)
		INSERT INTO Users
		(
			type,
			nick,
			password,
			date_registration,
			fio,
			birthday
		)
		values
		(
			1,
			@nick,
			@password,
			SYSDATETIME(),
			@fio,
			@birthday
		)
COMMIT TRANSACTION
GO