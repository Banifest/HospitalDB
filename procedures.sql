GO
CREATE PROCEDURE [dbo].[get_current_state_health]
    @login    NVARCHAR(50),
    @password NVARCHAR(50)
AS
  DECLARE param_cursor CURSOR LOCAL READ_ONLY FOR
    SELECT
      Examinations.name,
      Examinations.param
    FROM Patients, Examinations, Users
    WHERE Users.nick = @login AND Users.password = @password
          AND Patients.user_id = Users.id AND Examinations.patient_id = Patients.id
    ORDER BY Examinations.check_date DESC;

  CREATE TABLE #tmp (
    name NVARCHAR(50),
    par  NVARCHAR(50),
    val  NVARCHAR(50)
  );
  DECLARE @params XML;
  DECLARE @name NVARCHAR(50);

  OPEN param_cursor;

  FETCH NEXT FROM param_cursor
  INTO @name, @params;

  WHILE @@FETCH_STATUS = 0
    BEGIN

      DECLARE temp_cursor CURSOR LOCAL READ_ONLY FOR
        SELECT
          @name,
          Tbl.Col.value('name[1]', 'nvarchar(50)')  AS name,
          Tbl.Col.value('value[1]', 'nvarchar(50)') AS value
        FROM @params.nodes('//row') Tbl(Col);

      OPEN temp_cursor;


      DECLARE @exm_name NVARCHAR(50);
      DECLARE @exm_par NVARCHAR(50);
      DECLARE @exm_val NVARCHAR(50);

      FETCH NEXT FROM temp_cursor
      INTO @exm_name, @exm_par, @exm_val;

      WHILE @@FETCH_STATUS = 0
        BEGIN
          INSERT INTO #tmp SELECT
                             @exm_name,
                             @exm_par,
                             @exm_val
                           WHERE NOT EXISTS(SELECT TOP (1) *
                                            FROM #tmp
                                            WHERE #tmp.name = @exm_name AND #tmp.par = @exm_par)

          FETCH NEXT FROM temp_cursor
          INTO @exm_name, @exm_par, @exm_val;
        END;
      CLOSE temp_cursor;
      DEALLOCATE temp_cursor;

      FETCH NEXT FROM param_cursor
      INTO @name, @params;
    END;

  SELECT *
  FROM #tmp;

  DROP TABLE #tmp;
 GO
  --------------------------------------------------------------
  CREATE PROCEDURE [dbo].get_statistic_by_all_time
  AS
    SELECT *
    FROM (
           SELECT
             name_disease,
               YearMounth = DATENAME(MONTH, begin_date)
           FROM Diseases
         ) t
         PIVOT (
           COUNT(YearMounth)
         FOR YearMounth
         IN (
             January, February, March, April, May, June, July, August, September, October, November, December
         )
         ) p
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[get_statistic_by_index]
@index int
AS
SELECT *
FROM (
    SELECT
          name_disease
        , YearMounth = DATENAME(MONTH, begin_date)
    FROM Diseases, Patients, Hospitals WHERE Diseases.patient_id=Patients.id and Patients.hospital_id=Hospitals.id
	and Hospitals.zip= @index
) t
PIVOT (
    COUNT(YearMounth)
    FOR YearMounth IN (
        January, February, March, April, May, June, July, August, September, October, November, December
    )
) p
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[get_statistic_by_index_year]
@index int,
@date date
AS
SELECT *
FROM (
    SELECT
          name_disease
        , YearMounth = DATENAME(MONTH, begin_date)
    FROM Diseases, Patients, Hospitals WHERE Diseases.patient_id=Patients.id and Patients.hospital_id=Hospitals.id
	and Hospitals.zip= @index and Diseases.begin_date>=@date and Diseases.end_date<=(DATEADD(YEAR, 1,@date))
) t
PIVOT (
    COUNT(YearMounth)
    FOR YearMounth IN (
        January, February, March, April, May, June, July, August, September, October, November, December
    )
) p
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[get_statistic_by_year]
@date date
AS
SELECT *
FROM (
    SELECT
          name_disease
        , YearMounth = DATENAME(MONTH, begin_date)
    FROM Diseases WHERE
	Diseases.begin_date>=@date and Diseases.end_date<=(DATEADD(YEAR, 1,@date))
) t
PIVOT (
    COUNT(YearMounth)
    FOR YearMounth IN (
        January, February, March, April, May, June, July, August, September, October, November, December
    )
) p
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[add_disease]
	@login nvarchar(50),
	@doc_login nvarchar(50),
	@doc_password nvarchar(50),
	@name nvarchar(50),
	@date_begin date,
	@date_end date,
	@desc nvarchar(MAX)
AS
	DECLARE @patient_id int = 0;
	DECLARE @doctor_id int = 0;

	SELECT top(1) @patient_id = Patients.id
	FROM Patients, (SELECT * FROM Users WHERE nick = @login) as curr_user
	WHERE Patients.user_id = curr_user.id;

	SELECT top(1) @doctor_id = Doctors.id
	FROM Doctors, (SELECT * FROM Users WHERE nick = @doc_login and @doc_password=password) as curr_user
	WHERE Doctors.user_id = curr_user.id;

	if(@patient_id != 0 and @doctor_id != 0)
	BEGIN
		INSERT INTO Diseases
		VALUES (@name, @date_begin, @date_end, @doctor_id, @patient_id, @desc)
		SELECT 0;
	END
	else
	select 212;
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[add_doctor]
    @fio nvarchar(50),
	@nick nvarchar(50),
	@password nvarchar(50),
	@birthday date,
	@added_description nvarchar(max)
AS
	DECLARE @check_nick int;
	SELECT @check_nick = count(*) FROM Users WHERE nick = @nick;
	if(@check_nick = 0)
	BEGIN
		INSERT INTO Users(type,	nick, password,	date_registration, fio, birthday)
		values(	3,	@nick,	@password,	SYSDATETIME(), @fio, @birthday)

		DECLARE @user_id int;
		SELECT @user_id = id FROM Users WHERE nick = @nick;

		INSERT INTO Doctors(user_id, added_description)
		VALUES(@user_id, @added_description);
		SELECT 0;
	END
	else
	select 203;
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[add_examination]
    @doc_login nvarchar(50),
	@doc_password nvarchar(50),
	@login nvarchar(50),
	@name nvarchar(50),
	@date date
AS
	DECLARE @doc_id int = 0;
	DECLARE @pat_id int = 0;

	SELECT top(1) @doc_id = Doctors.id FROM Doctors, Users
	WHERE nick = @doc_login and password = @doc_password
	and Doctors.user_id = Users.id;

	SELECT top(1) @pat_id = Patients.id FROM Patients, Users
	WHERE nick = @login and Patients.user_id = Users.id;


	if(@doc_id!=0 and @pat_id!=0)
	begin
		INSERT INTO Examinations
		(doctor_id,patient_id,param, check_date, name)
		values(@doc_id,@pat_id,'<root><empty id="0"></empty></root>', @date, @name);
		SELECT 0;
	end;
	else
	SELECT 219;
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[add_param]
	@id int,
	@doc_login nvarchar(50),
	@doc_password nvarchar(50),
	@name nvarchar(50),
	@val nvarchar(50)
AS
	DECLARE @doctor_id int = 0;

	SELECT top(1) @doctor_id = Doctors.id
	FROM Doctors, (SELECT * FROM Users WHERE nick = @doc_login and @doc_password=password) as curr_user
	WHERE Doctors.user_id = curr_user.id;

	if(@doctor_id!=0)
	BEGIN
		UPDATE Examinations
		SET param.modify('
		insert (<row><name>"{sql:variable("@name")}"</name><value>"{sql:variable("@name")}"</value></row>)
		after (//empty)[1]
		')
		WHERE id=@id;
		SELECT 0;
	END
	else
	select 217;
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[add_patient]
    @fio nvarchar(50),
	@gender bit,
	@hospital_zip int,
	@nick nvarchar(50),
	@password nvarchar(50),
	@birthday date
AS
	DECLARE @check_nick int;
	DECLARE @check_zip int;
	SELECT @check_nick = count(*) FROM Users WHERE nick = @nick;
	SELECT @check_zip = count(*) FROM Hospitals WHERE @hospital_zip=zip;
	print @check_zip;
	if (@check_zip =0) SELECT 202;
	else
	if(@check_nick = 0)
	BEGIN
		INSERT INTO Users(Users.type,nick,Users.password,date_registration,fio,birthday)
		values(1,@nick,@password,SYSDATETIME(),	@fio,@birthday);

		DECLARE @user_id int;

		SELECT @user_id = id FROM Users WHERE nick = @nick;

		DECLARE @hospital_id int;

		SELECT top(1) @hospital_id = id FROM Hospitals WHERE @hospital_zip=zip;


		INSERT INTO Patients(gender,hospital_id,user_id)
		VALUES(@gender,@hospital_id,@user_id);
		SELECT 0;
	END;
	else
	BEGIN
		SELECT 201;
	END
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[appoint_drag]
	@id int,
	@name nvarchar(50)
AS
	DECLARE @drag_id int = 0;
	SELECT top(1) @drag_id = Drags.id
	FROM Drags
	WHERE name=@name;

	DECLARE @dragdisease_id int = 0;

	SELECT @dragdisease_id = count(*)
	FROM DiseasesDrags
	WHERE @id=disease_id and @drag_id=drag_id;

	if(@drag_id!=0 and @dragdisease_id=0)
	BEGIN
		INSERT INTO DiseasesDrags
		VALUES(@id, @drag_id);
		SELECT 0;
	END
	else
	select 214;
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[auth_user]
	@login nvarchar(50),
	@password nvarchar(50)
AS
    SELECT * FROM Users
	WHERE @login=Users.nick and @password=Users.password;
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[change_disease]
	@id int,
	@date_end date
AS
	declare @begin_date date = NULL;
	SELECT top(1) @begin_date= Diseases.begin_date FROM Diseases WHERE Diseases.id=@id;

	if(@begin_date<@date_end)
	BEGIN
		UPDATE Diseases
		SET end_date = @date_end
		WHERE Diseases.id = @id;
		SELECT 0;
	END
	else
	select 213;
GO
--------------------------------------------------------------
CREATE  PROCEDURE [dbo].[change_patient]
	@login nvarchar(50),
	@zip int
AS
	DECLARE @patient_id int = 0;
	DECLARE @hospital_id int = 0;

	SELECT top(1) @patient_id = Patients.id
	FROM Patients, (SELECT * FROM Users WHERE nick = @login) as curr_user
	WHERE Patients.user_id = curr_user.id;

	SELECT top(1) @hospital_id = Hospitals.id FROM Hospitals WHERE zip=@zip;

	if(@patient_id!=0 and @hospital_id!=0)
	BEGIN
		UPDATE Patients
		SET hospital_id = @hospital_id
		WHERE id = @patient_id;

		SELECT 0;
	END
	else
	select 205;
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[del_doctor]
	@login nvarchar(50),
	@zip int
AS
	DECLARE @check_type int;
	DECLARE @doctor_id int = 0;
	DECLARE @hospital_id int = 0;
	DECLARE @doctorhospital_id int = 0;
	SELECT top(1) @check_type = Users.type FROM Users WHERE nick = @login;

	SELECT top(1) @doctor_id = Doctors.id
	FROM Doctors, (SELECT * FROM Users WHERE nick = @login) as curr_user
	WHERE Doctors.user_id = curr_user.id;

	SELECT top(1) @hospital_id = Hospitals.id FROM Hospitals WHERE zip=@zip;

	SELECT top(1) @doctorhospital_id = DoctorsHospitals.id FROM DoctorsHospitals
	WHERE hospital_id=@hospital_id and @doctor_id=doctor_id;

	if(@check_type = 1 and @doctorhospital_id != 0)
	BEGIN
		UPDATE top(1)  DoctorsHospitals
		SET date_end_working=GETDATE()
		WHERE @doctorhospital_id = DoctorsHospitals.id;
		SELECT 0;
	END
	else
	select 206;
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[get_current_state_health]
	@login nvarchar(50),
	@password nvarchar(50)
AS
	DECLARE param_cursor cursor local read_only for
	SELECT Examinations.name, Examinations.param
	FROM Patients, Examinations, Users
	WHERE Users.nick=@login and Users.password=@password
	and Patients.user_id=Users.id and Examinations.patient_id=Patients.id
	ORDER BY Examinations.check_date DESC;

	CREATE TABLE #tmp (name nvarchar(50), par nvarchar(50), val nvarchar(50));
	DECLARE @params xml;
	DECLARE @name nvarchar(50);

	open param_cursor;

	fetch next from param_cursor into @name, @params;

	while @@FETCH_STATUS = 0
	begin

		DECLARE temp_cursor cursor local read_only for
		SELECT
		@name,
        Tbl.Col.value('name[1]', 'nvarchar(50)') as name,
        Tbl.Col.value('value[1]', 'nvarchar(50)') as value
		FROM   @params.nodes('//row') Tbl(Col);

		open temp_cursor;


		DECLARE @exm_name nvarchar(50);
		DECLARE @exm_par nvarchar(50);
		DECLARE @exm_val nvarchar(50);

		fetch next from temp_cursor into @exm_name, @exm_par, @exm_val;

		while @@FETCH_STATUS = 0
		begin
			INSERT INTO #tmp SELECT @exm_name, @exm_par, @exm_val
			WHERE NOT EXISTS(SELECT top(1) * FROM #tmp WHERE #tmp.name=@exm_name and #tmp.par=@exm_par)

			fetch next from temp_cursor into @exm_name, @exm_par, @exm_val;
		end;
		close temp_cursor;
		DEALLOCATE temp_cursor;

		fetch next from param_cursor into  @name, @params;
	end;

	SELECT * FROM #tmp;

	DROP TABLE #tmp;
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[get_doctor_examination_param]
	@login nvarchar(50),
	@password nvarchar(50),
	@id int
AS
	DECLARE @x xml;
	DECLARE @name nvarchar(50) = '';

	SELECT @x=Examinations.param, @name= Examinations.name
	FROM Examinations, Doctors, (SELECT top(1) * FROM Users WHERE password=@password and @login=nick) as curr_user
	WHERE Examinations.id=@id and Doctors.user_id=curr_user.id and Examinations.doctor_id=Doctors.id;

	SELECT
	   @name,
       Tbl.Col.value('name[1]', 'nvarchar(50)') as 'Param name',
       Tbl.Col.value('value[1]', 'nvarchar(50)') as 'Param value'
	FROM   @x.nodes('//row') Tbl(Col);
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[get_doctor_examinations]
	@login nvarchar(50),
	@doc_login nvarchar(50),
	@doc_password nvarchar(50),
	@date_begin date,
	@date_end date
AS
	DECLARE @pat_id int = 0;
	DECLARE @doc_id int = 0;

	SELECT top(1) @pat_id = Patients.id FROM Users, Patients
	WHERE nick = @login and Patients.user_id=Users.id;

	SELECT top(1) @doc_id = Doctors.id FROM Users, Doctors
	WHERE nick = @doc_login and password=@doc_password and Doctors.user_id=Users.id;

	if (@doc_id!=0 and @pat_id!=0)
	begin
		SELECT id, check_date, name FROM Examinations
		WHERE doctor_id=@doc_id and patient_id=@pat_id
		and @date_begin < Examinations.check_date and @date_end > Examinations.check_date;
	end;
	else
		SELECT 217;
GO
--------------------------------------------------------------
CREATE  PROCEDURE [dbo].[get_drag_by_id]
	@id int
AS
	SELECT  Drags.id, Drags.name, Drags.price, Drags.shelf_life, Drags.description, Drags.mass, Drags.provider, Drags.is_need_recipe
	FROM Drags
	WHERE id=@id;
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[get_drag_by_name]
	@name nvarchar(50)
AS
	SELECT Drags.id, Drags.name, Drags.price, Drags.shelf_life, Drags.description, Drags.mass, Drags.provider, Drags.is_need_recipe
	FROM Drags
	WHERE name=@name;
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[get_drags_by_disease]
	@login nvarchar(50),
	@password nvarchar(50),
	@id int
AS
	SELECT Drags.id, Drags.name, Drags.price, Drags.shelf_life, Drags.description, Drags.mass, Drags.provider, Drags.is_need_recipe
	FROM (SELECT top(1) Diseases.id
	FROM Patients, Diseases, (SELECT top(1) * FROM Users WHERE @login=nick) as curr_user
	WHERE @id = Diseases.id and curr_user.id = Patients.user_id and Patients.id = Diseases.patient_id)
	 as curr_disease, DiseasesDrags, Drags
	WHERE curr_disease.id=DiseasesDrags.disease_id and Drags.id=DiseasesDrags.drag_id;
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[get_drags_by_disease_doctor]
	@login nvarchar(50),
	@password nvarchar(50),
	@id int
AS
	SELECT Drags.id, Drags.name, Drags.price, Drags.shelf_life, Drags.description, Drags.mass, Drags.provider, Drags.is_need_recipe
	FROM (SELECT top(1) Diseases.id
	FROM Doctors, Diseases, (SELECT top(1) * FROM Users WHERE password=@password and @login=nick) as curr_user
	WHERE @id = Diseases.id and curr_user.id = Doctors.user_id and Doctors.id = Diseases.doctor_id)
	as curr_disease, DiseasesDrags, Drags
	WHERE curr_disease.id=DiseasesDrags.disease_id and Drags.id=DiseasesDrags.drag_id;
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[get_exclude_doctor_examinations]
	@login nvarchar(50),
	@doc_login nvarchar(50),
	@doc_password nvarchar(50),
	@date_begin date,
	@date_end date
AS
	DECLARE @pat_id int = 0;
	DECLARE @doc_id int = 0;

	SELECT top(1) @pat_id = Patients.id FROM Users, Patients
	WHERE nick = @login and Patients.user_id=Users.id;

	SELECT top(1) @doc_id = Doctors.id FROM Users, Doctors
	WHERE nick = @doc_login and password=@doc_password and Doctors.user_id=Users.id;

	if (@doc_id!=0 and @pat_id!=0)
	begin
		SELECT id, check_date, name FROM Examinations
		WHERE doctor_id=@doc_id and patient_id=@pat_id
		and (@date_begin > Examinations.check_date or @date_end < Examinations.check_date);
	end;
	else
		SELECT 217;
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[get_exclude_doctor_examinations]
	@login nvarchar(50),
	@doc_login nvarchar(50),
	@doc_password nvarchar(50),
	@date_begin date,
	@date_end date
AS
	DECLARE @pat_id int = 0;
	DECLARE @doc_id int = 0;

	SELECT top(1) @pat_id = Patients.id FROM Users, Patients
	WHERE nick = @login and Patients.user_id=Users.id;

	SELECT top(1) @doc_id = Doctors.id FROM Users, Doctors
	WHERE nick = @doc_login and password=@doc_password and Doctors.user_id=Users.id;

	if (@doc_id!=0 and @pat_id!=0)
	begin
		SELECT id, check_date, name FROM Examinations
		WHERE doctor_id=@doc_id and patient_id=@pat_id
		and (@date_begin > Examinations.check_date or @date_end < Examinations.check_date);
	end;
	else
		SELECT 217;
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[get_inverse_patient_diseases]
	@login nvarchar(50),
	@password nvarchar(50),
	@date_begining date,
	@date_ending date
AS
	SELECT Diseases.id, Diseases.name_disease, Diseases.begin_date, Diseases.end_date, Diseases.patient_id
	FROM Patients, Diseases, (SELECT top(1) * FROM Users WHERE password=@password and @login=nick) as curr_user
	WHERE curr_user.id = Patients.user_id and Patients.id = Diseases.patient_id
	and (@date_begining>Diseases.end_date or @date_ending<Diseases.begin_date);
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[get_inverse_patient_examinations]
	@login nvarchar(50),
	@password nvarchar(50),
	@date_begin date,
	@date_end date
AS
	DECLARE @pat_id int = 0;

	SELECT top(1) @pat_id = Patients.id FROM Users, Patients
	WHERE nick = @login and @password = password and Patients.user_id=Users.id;

	if (@pat_id!=0)
	begin
		SELECT Examinations.id, check_date, name, Users.fio
		FROM Examinations, Doctors, Users
		WHERE patient_id=@pat_id and Examinations.doctor_id = Doctors.id and Users.id = Doctors.user_id
		and (@date_begin > Examinations.check_date or @date_end < Examinations.check_date);
	end;
	else
		SELECT 250;
GO
--------------------------------------------------------------
CREATE  PROCEDURE [dbo].[get_param_examination]
	@login nvarchar(50),
	@password nvarchar(50),
	@id int
AS
	DECLARE @x xml;
	DECLARE @name nvarchar(50) = '';

	SELECT @x=Examinations.param, @name= Examinations.name
	FROM Examinations, Patients, (SELECT top(1) * FROM Users WHERE password=@password and @login=nick) as curr_user
	WHERE Examinations.id=@id and Patients.user_id=curr_user.id and Examinations.patient_id=Patients.id;

	SELECT
	   @name,
       Tbl.Col.value('name[1]', 'nvarchar(50)') as 'Param name',
       Tbl.Col.value('value[1]', 'nvarchar(50)') as 'Param value'
	FROM   @x.nodes('//row') Tbl(Col);
GO
--------------------------------------------------------------
CREATE  PROCEDURE [dbo].[get_patient]
	@login nvarchar(50),
	@password nvarchar(50)
AS
	SELECT top(1) curr_user.fio, curr_user.birthday, Patients.gender, Hospitals.address
	FROM Hospitals, Patients, (SELECT top(1) * FROM Users WHERE password=@password and @login=nick) as curr_user
	WHERE curr_user.id = Patients.user_id and Hospitals.id=Patients.hospital_id;
GO
--------------------------------------------------------------
CREATE PROCEDURE [dbo].[get_patient_diseases]
	@login nvarchar(50),
	@password nvarchar(50),
	@date_begining date,
	@date_ending date
AS
	SELECT Diseases.id, Diseases.name_disease, Diseases.begin_date, Diseases.end_date, Diseases.patient_id
	FROM Patients, Diseases, (SELECT top(1) * FROM Users WHERE password=@password and @login=nick) as curr_user
	WHERE curr_user.id = Patients.user_id and Patients.id = Diseases.patient_id
	and @date_begining<Diseases.end_date and @date_ending>Diseases.begin_date;
GO
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[get_patient_examinations]
	@login nvarchar(50),
	@password nvarchar(50),
	@date_begin date,
	@date_end date
AS
	DECLARE @pat_id int = 0;

	SELECT top(1) @pat_id = Patients.id FROM Users, Patients
	WHERE nick = @login and @password = password and Patients.user_id=Users.id;

	if (@pat_id!=0)
	begin
		SELECT Examinations.id, check_date, name, Users.fio
		FROM Examinations, Doctors, Users
		WHERE patient_id=@pat_id and Examinations.doctor_id = Doctors.id and Users.id = Doctors.user_id
		and @date_begin < Examinations.check_date and @date_end > Examinations.check_date;
	end;
	else
		SELECT 250;
GO
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[is_auth_user]
	@login nvarchar(50),
	@password nvarchar(50)
AS
    SELECT count(*) FROM Users
	WHERE @login=Users.nick and @password=Users.password;
GO
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[see_exm_doc]
	@login nvarchar(50),
	@doc_login nvarchar(50),
	@doc_password nvarchar(50)
AS
	DECLARE @patient_id int = 0;
	DECLARE @doctor_id int = 0;

	SELECT top(1) @patient_id = Patients.id
	FROM Patients, (SELECT * FROM Users WHERE nick = @login) as curr_user
	WHERE Patients.user_id = curr_user.id;

	SELECT top(1) @doctor_id = Doctors.id
	FROM Doctors, (SELECT * FROM Users WHERE nick = @doc_login and @doc_password=password) as curr_user
	WHERE Doctors.user_id = curr_user.id;

	if(@doctor_id!=0 and @patient_id!=0)
	BEGIN
		SELECT * FROM Examinations
		WHERE doctor_id=@doctor_id and patient_id=@patient_id;
	END
	else
	select 216;
GO
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[select_disease]
	@login nvarchar(50),
	@doc_login nvarchar(50),
	@doc_password nvarchar(50)
AS
	DECLARE @patient_id int = 0;
	DECLARE @doctor_id int = 0;

	SELECT top(1) @patient_id = Patients.id
	FROM Patients, (SELECT * FROM Users WHERE nick = @login) as curr_user
	WHERE Patients.user_id = curr_user.id;

	SELECT top(1) @doctor_id = Doctors.id
	FROM Doctors, (SELECT * FROM Users WHERE nick = @doc_login and @doc_password=password) as curr_user
	WHERE Doctors.user_id = curr_user.id;

	if(@patient_id != 0 and @doctor_id != 0)
	BEGIN
		SELECT Id, name_disease, begin_date, end_date, Diseases.description FROM Diseases
		WHERE @patient_id=Diseases.patient_id and @doctor_id=Diseases.doctor_id;
	END
	else
	select 211;
GO
-------------------------------------------------------------
 PROCEDURE [dbo].[take_doctor]
	@login nvarchar(50),
	@zip int,
	@spec nvarchar(50),
	@begin_date date,
	@begin_time time(7),
	@end_time time(7)
AS
	DECLARE @check_type int;
	DECLARE @doctor_id int = 0;
	DECLARE @hospital_id int = 0;
	SELECT top(1) @check_type = Users.type FROM Users WHERE nick = @login;

	SELECT top(1) @doctor_id = Doctors.id
	FROM Doctors, (SELECT * FROM Users WHERE nick = @login) as curr_user
	WHERE Doctors.user_id = curr_user.id;

	SELECT top(1) @hospital_id = Hospitals.id FROM Hospitals WHERE zip=@zip;

	if(@check_type = 3 and @doctor_id!=0 and @hospital_id!=0)
	BEGIN
		INSERT INTO DoctorsHospitals
		VALUES(@begin_date, NULL, @doctor_id, @hospital_id, @spec, @begin_time, @end_time)
		SELECT 0;
	END
	else
	select 204;
GO
-------------------------------------------------------------
-------------------------------------------------------------