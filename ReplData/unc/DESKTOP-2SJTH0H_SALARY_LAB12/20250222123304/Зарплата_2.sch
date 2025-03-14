drop Table [dbo].[Зарплата]
go
SET ANSI_PADDING OFF
go

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Зарплата](
	[ФИО] [nvarchar](50) NOT NULL,
	[Должность] [nvarchar](50) NOT NULL,
	[Стаж, лет] [int] NOT NULL,
	[Оклад, руб] [float] NOT NULL,
	[Премия, руб] [float] NOT NULL,
	[Надбавка за стаж, руб] [float] NOT NULL,
	[Итого, руб] [float] NOT NULL,
	[Налоги, руб] [float] NOT NULL,
	[Получить, руб] [float] NOT NULL,
	[rowguid] [uniqueidentifier] ROWGUIDCOL  NOT NULL
)

GO
ALTER TABLE [dbo].[Зарплата] ADD  CONSTRAINT [DF__Зарплата__ФИО__36B12243]  DEFAULT ('---') FOR [ФИО]
GO
ALTER TABLE [dbo].[Зарплата] ADD  CONSTRAINT [DF__Зарплата__Должно__37A5467C]  DEFAULT ('---') FOR [Должность]
GO
ALTER TABLE [dbo].[Зарплата] ADD  CONSTRAINT [DF__Зарплата__Стаж, __38996AB5]  DEFAULT ((0)) FOR [Стаж, лет]
GO
ALTER TABLE [dbo].[Зарплата] ADD  CONSTRAINT [DF__Зарплата__Оклад,__398D8EEE]  DEFAULT ((0)) FOR [Оклад, руб]
GO
ALTER TABLE [dbo].[Зарплата] ADD  CONSTRAINT [DF__Зарплата__Премия__3A81B327]  DEFAULT ((0)) FOR [Премия, руб]
GO
ALTER TABLE [dbo].[Зарплата] ADD  CONSTRAINT [DF__Зарплата__Надбав__3B75D760]  DEFAULT ((0)) FOR [Надбавка за стаж, руб]
GO
ALTER TABLE [dbo].[Зарплата] ADD  CONSTRAINT [DF__Зарплата__Итого,__3C69FB99]  DEFAULT ((0)) FOR [Итого, руб]
GO
ALTER TABLE [dbo].[Зарплата] ADD  CONSTRAINT [DF__Зарплата__Налоги__3D5E1FD2]  DEFAULT ((0)) FOR [Налоги, руб]
GO
ALTER TABLE [dbo].[Зарплата] ADD  CONSTRAINT [DF__Зарплата__Получи__3E52440B]  DEFAULT ((0)) FOR [Получить, руб]
GO
ALTER TABLE [dbo].[Зарплата] ADD  CONSTRAINT [MSmerge_df_rowguid_CFDD9671D31047A6B9591A68EF848AF8]  DEFAULT (newsequentialid()) FOR [rowguid]
GO
SET ANSI_NULLS ON

go

SET QUOTED_IDENTIFIER ON

go

