USE [test]
GO
CREATE TABLE [dbo].[Users](
	[id] [int] IDENTITY(1,1) primary key NOT NULL,
	[type] [int] NOT NULL,
	[nick] [nvarchar](50) NOT NULL,
	[password] [nvarchar](50) NOT NULL,
	[date_registration] [date] NOT NULL,
	[fio] [nvarchar](50) NOT NULL,
	[birthday] [date] NOT NULL)
GO
CREATE TABLE [dbo].[Patients](
	[id] [int] IDENTITY(1,1) primary key NOT NULL,
	[gender] [bit] NULL,
	[hospital_id] [int] NOT NULL,
	[user_id] [int] NOT NULL,
	 CONSTRAINT [FK_Patient_Hospital] FOREIGN KEY([hospital_id])
REFERENCES [dbo].[Hospitals] ([id]))
GO
CREATE TABLE [dbo].[Doctors](
	[id] [int] IDENTITY(1,1) primary key NOT NULL,
	[added_description] [nvarchar](max) NULL,
	[user_id] [int] NOT NULL,
CONSTRAINT [FK_Doctors_Users] FOREIGN KEY([user_id])
REFERENCES [dbo].[Users] ([id]))
GO

CREATE TABLE [dbo].[Hospitals](
	[id] [int] IDENTITY(1,1) primary key NOT NULL,
	[address] [nvarchar](50) NOT NULL,
	[zip] [int] NOT NULL,
	[phone] [nvarchar](15) NOT NULL,
	[main_doctor] [int] NOT NULL,
	CONSTRAINT [FK_Hospitals_Doctors] FOREIGN KEY([main_doctor])
REFERENCES [dbo].[Doctors] ([id]))

GO

CREATE TABLE [dbo].[Drags](
	[id] [int] IDENTITY(1,1) primary key NOT NULL,
	[name] [nvarchar](50) NOT NULL,
	[price] [money] NOT NULL,
	[shelf_life] [date] NOT NULL,
	[description] [nvarchar](max) NOT NULL,
	[mass] [real] NOT NULL,
	[provider] [nvarchar](50) NOT NULL,
	[is_need_recipe] [bit] NULL)
GO

CREATE TABLE [dbo].[Examinations](
	[id] [int] IDENTITY(1,1) primary key NOT NULL,
	[doctor_id] [int] NOT NULL,
	[param] [xml] NOT NULL,
	[patient_id] [int] NOT NULL,
	[check_date] [date] NOT NULL,
	[name] [nvarchar](50) NULL,
	CONSTRAINT [FK_Examinations_Doctors] FOREIGN KEY([doctor_id])
	REFERENCES [dbo].[Doctors] ([id]),
	CONSTRAINT [FK_Examinations_Patients] FOREIGN KEY([patient_id])
	REFERENCES [dbo].[Patients] ([id]))
GO

CREATE TABLE [dbo].[Diseases](
	[id] [int] IDENTITY(1,1) primary key NOT NULL,
	[name_disease] [nvarchar](50) NOT NULL,
	[begin_date] [date] NOT NULL,
	[end_date] [date] NOT NULL,
	[doctor_id] [int] NOT NULL,
	[patient_id] [int] NOT NULL,
	[description] [nvarchar](max) NULL,
	CONSTRAINT [FK_Diseases_Patients] FOREIGN KEY([patient_id])
	REFERENCES [dbo].[Patients] ([id]))
GO

CREATE TABLE [dbo].[DiseasesDrags](
	[id] [int] IDENTITY(1,1) primary key NOT NULL,
	[disease_id] [int] NOT NULL,
	[drag_id] [int] NOT NULL,
	CONSTRAINT [disease] FOREIGN KEY([disease_id])
	REFERENCES [dbo].[Diseases] ([id]),
	CONSTRAINT [drag] FOREIGN KEY([drag_id])
	REFERENCES [dbo].[Drags] ([id]))
GO

CREATE TABLE [dbo].[DoctorsHospitals](
	[id] [int] IDENTITY(1,1) primary key NOT NULL,
	[doctor_id] [int] NULL,
	[hospital_id] [int] NULL,
	[speciality] [nvarchar](50) NOT NULL,
	[time_begin_working] [time](7) NULL,
	[time_end_working] [time](7) NULL,
	[date_begin_working] [date] NULL,
	[date_end_working] [date] NULL,
	CONSTRAINT [FK_DoctorsHospitals_Doctors] FOREIGN KEY([doctor_id])
	REFERENCES [dbo].[Doctors] ([id]),
	CONSTRAINT [FK_DoctorsHospitals_Hospitals] FOREIGN KEY([hospital_id])
	REFERENCES [dbo].[Hospitals] ([id]))
GO