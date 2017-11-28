import pyodbc


def connection_to_db(username: str = 'test', password: str = '123'):
    server = 'localhost'
    database = 'test'
    connection_string = 'DRIVER={0};SERVER={1};DATABASE={2};UID={3};PWD={4}'.format(
        'ODBC Driver 13 for SQL Server', server, database, username, password
    )
    return pyodbc.connect(connection_string)


conn = connection_to_db()
cursor = conn.cursor()
cursor.execute("EXEC [get_patient_diseases] 'banifest', '123', '1990-01-01', '3000-01-01';")
row = cursor.fetchone()
print(row)