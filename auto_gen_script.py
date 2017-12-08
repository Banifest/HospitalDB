import random

from client.model.dbConnect import connection_to_db

conn = connection_to_db('test', '123')
cursor = conn.cursor()
MAN_NAMES = ["Алексанлдр", "Алексей", "Владислав", "Владимир", "Петр", "Василий"]
WOMAN_NAMES = ["Оксана", "Ольга", "Татьяна", "Ксения", "Екатерина", "Елизавета"]

SURNAMES = ["Петров", "Сидоров", "Смирнов", "Иванов", "Сычевский", "Бударевский"]

# MAN_FIO = ["{0} {1}".format(random.choice(MAN_NAMES), random.choice(SURNAMES)) for x in range(0, 5000)]

# WOMAN_FIO = ["{0} {1}".format(random.choice(WOMAN_NAMES), random.choice(SURNAMES)) for x in range(0, 5000)]

file = open('script.sql', "w")
counter = 90000
# for x in MAN_FIO:
#     counter += 1
#     cursor.execute("""EXEC [add_patient] '{0}', 1, '{1}', '{2}', '{3}', '{4}';""".format(
#         x, 12345, str(counter) + x, 123, '01-01-{2}'.format(
#             random.randint(1, 28), random.randint(1, 12), random.randint(1900, 2017)
#         )
#     ))
#
# for x in WOMAN_FIO:
#     counter += 1
#     cursor.execute("""EXEC [add_patient] '{0}', 0, '{1}', '{2}', '{3}', '{4}';""".format(
#         x, 220000, str(counter) + x, 123, '01-01-{2}'.format(
#             random.randint(1, 28), random.randint(1, 12), random.randint(1900, 2017)
#         )
#     ))
#
# for x in range(100):
#     cursor.execute("""EXEC add_doctor 1, '2100-12-31'""".format(
#         'doctor ' + MAN_FIO[x], str(x) + "doc", 123, "01-01-{2}".format(
#             random.randint(1, 28), random.randint(1, 12), random.randint(1900, 2017)), "это доктор"
#     ))

for x in range(1000):
    cursor.execute("""INSERT INTO [dbo].[Drags]
           ([name]
           ,[price]
           ,[shelf_life]
           ,[description]
           ,[mass]
           ,[provider]
           ,[is_need_recipe])
     VALUES
           ('{0}', {1}, '{2}', '{3}', {4}, '{5}', {6})""".format(
        random.choice(["Пара", "Ксино", "Дека"]) + random.choice(["медо", "цито", "ро"]) + random.choice(
            ["мол", "вол", "кол"]),
        random.randint(1, 1000),
        "{2}-{1}-{0}".format(random.randint(1, 28), random.randint(1, 12), random.randint(2018, 3000)),
        "Описание",
        random.randint(10, 10000),
        "Аптека",
        random.randint(0, 1)
    ))
