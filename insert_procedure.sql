USE [hospital]
GO
CREATE PROCEDURE dbo.add_patient 
    @fio nvarchar(50),
	@gender bit,
	@hospital_id int,
	@nick nvarchar(50), 
	@password nvarchar(50),
	@birthday date 
AS
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
		return -1

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
		return -1

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
GO
	CREATE PROCEDURE dbo.add_hospital 
    @address nvarchar(50),
	@zip int,
	@phone nvarchar(15), 
	@main_doctor int
AS
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
GO