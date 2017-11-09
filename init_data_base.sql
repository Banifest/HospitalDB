USE [hospital]
GO
CREATE TABLE [dbo].[Users](
	[id] [int] NOT NULL,
	[type] [int] NOT NULL,
	[nick] [nvarchar](50) NOT NULL,
	[password] [nvarchar](50) NOT NULL,
	[date_registration] [date] NOT NULL,
	[fio] [nvarchar](50) NOT NULL,
	[birthday] [date] NOT NULL,
 CONSTRAINT [PK_Users_1] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[Doctors](
	[id] [int] NOT NULL,
	[specialty] [nvarchar](50) NOT NULL,
	[hospital_id] [int] NOT NULL,
	[position_type] [int] NOT NULL,
	[added_description] [nvarchar](max) NULL,
	[user_id] [int] NOT NULL,
 CONSTRAINT [PK_Doctors_1] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

CREATE TABLE [dbo].[Patients](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[gender] [bit] NULL,
	[hospital_id] [int] NOT NULL,
	[user_id] [int] NOT NULL,
 CONSTRAINT [PK_Patient_1] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[Diseases](
	[id] [int] NOT NULL,
	[name_disease] [nvarchar](50) NOT NULL,
	[begin_date] [date] NOT NULL,
	[end_date] [date] NOT NULL,
	[doctor_id] [int] NOT NULL,
	[patient_id] [int] NOT NULL,
 CONSTRAINT [PK_Disease_1] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[DiseasesDrags](
	[id] [int] NOT NULL,
	[disease_id] [int] NOT NULL,
	[drag_id] [int] NOT NULL,
 CONSTRAINT [PK_DiseasesDrags] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[Drags](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](50) NOT NULL,
	[price] [money] NOT NULL,
	[shelf_life] [date] NOT NULL,
	[description] [nvarchar](max) NOT NULL,
	[mass] [real] NOT NULL,
	[provider] [nvarchar](50) NOT NULL,
	[is_need_recipe] [bit] NULL,
 CONSTRAINT [PK_Drags_1] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

CREATE TABLE [dbo].[Examinations](
	[id] [int] NOT NULL,
	[doctor_id] [int] NOT NULL,
	[param] [xml] NOT NULL,
	[value] [nvarchar](50) NOT NULL,
	[patient_id] [int] NOT NULL,
 CONSTRAINT [PK_Examination_1] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

CREATE TABLE [dbo].[Hospitals](
	[id] [int] NOT NULL,
	[address] [nvarchar](50) NOT NULL,
	[zip] [int] NOT NULL,
	[phone] [nvarchar](15) NOT NULL,
	[main_doctor] [int] NOT NULL,
 CONSTRAINT [PK_Hospital] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO



ALTER TABLE [dbo].[Hospitals]  WITH CHECK ADD  CONSTRAINT [FK_Hospitals_Doctors] FOREIGN KEY([main_doctor])
REFERENCES [dbo].[Doctors] ([id])
GO

ALTER TABLE [dbo].[Hospitals] CHECK CONSTRAINT [FK_Hospitals_Doctors]
GO

ALTER TABLE [dbo].[Examinations]  WITH CHECK ADD  CONSTRAINT [FK_Examinations_Doctors] FOREIGN KEY([doctor_id])
REFERENCES [dbo].[Doctors] ([id])
GO

ALTER TABLE [dbo].[Examinations] CHECK CONSTRAINT [FK_Examinations_Doctors]
GO

ALTER TABLE [dbo].[Examinations]  WITH CHECK ADD  CONSTRAINT [FK_Examinations_Patients] FOREIGN KEY([patient_id])
REFERENCES [dbo].[Patients] ([id])
GO

ALTER TABLE [dbo].[Examinations] CHECK CONSTRAINT [FK_Examinations_Patients]
GO



ALTER TABLE [dbo].[DiseasesDrags]  WITH CHECK ADD  CONSTRAINT [disease] FOREIGN KEY([disease_id])
REFERENCES [dbo].[Diseases] ([id])
GO

ALTER TABLE [dbo].[DiseasesDrags] CHECK CONSTRAINT [disease]
GO

ALTER TABLE [dbo].[DiseasesDrags]  WITH CHECK ADD  CONSTRAINT [drag] FOREIGN KEY([drag_id])
REFERENCES [dbo].[Drags] ([id])
GO

ALTER TABLE [dbo].[DiseasesDrags] CHECK CONSTRAINT [drag]
GO

ALTER TABLE [dbo].[Diseases]  WITH CHECK ADD  CONSTRAINT [FK_Diseases_Patients] FOREIGN KEY([patient_id])
REFERENCES [dbo].[Patients] ([id])
GO

ALTER TABLE [dbo].[Diseases] CHECK CONSTRAINT [FK_Diseases_Patients]
GO



ALTER TABLE [dbo].[Patients] SET (LOCK_ESCALATION = AUTO)
GO

ALTER TABLE [dbo].[Patients]  WITH CHECK ADD  CONSTRAINT [FK_Patient_Hospital] FOREIGN KEY([hospital_id])
REFERENCES [dbo].[Hospitals] ([id])
GO

ALTER TABLE [dbo].[Patients] CHECK CONSTRAINT [FK_Patient_Hospital]
GO

ALTER TABLE [dbo].[Patients]  WITH CHECK ADD  CONSTRAINT [FK_Patients_Users] FOREIGN KEY([user_id])
REFERENCES [dbo].[Users] ([id])
GO

ALTER TABLE [dbo].[Patients] CHECK CONSTRAINT [FK_Patients_Users]
GO





ALTER TABLE [dbo].[Doctors]  WITH CHECK ADD  CONSTRAINT [FK_Doctors_Users] FOREIGN KEY([user_id])
REFERENCES [dbo].[Users] ([id])
GO

ALTER TABLE [dbo].[Doctors] CHECK CONSTRAINT [FK_Doctors_Users]
GO