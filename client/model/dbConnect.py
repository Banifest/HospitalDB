import pymssql


def connection_to_db(username: str = 'reg', password: str = 'reg'):
    return pymssql.connect(server='localhost', user=username, password=password, database="test", port='1434',
                           autocommit=True)
