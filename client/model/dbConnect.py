import pyodbc
import pymssql

# def connection_to_db(username: str = 'test', password: str = '123'):
#     server = 'localhost'
#     database = 'test'
#     connection_string = 'DRIVER={0};SERVER={1};DATABASE={2};UID={3};PWD={4}'.format(
#         'ODBC Driver 13 for SQL Server', server, database, username, password
#     )
#     return pyodbc.connect(connection_string)


def connection_to_db(username: str = 'test', password: str = '123'):
    conn = pymssql.connect(server='localhost', user='test', password='123', database="test", port='1434',
                           autocommit=True)
    return conn
