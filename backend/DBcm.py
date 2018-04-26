"""
Simple example usage:

    from DBcm import UseDatabase, SQLError

    config = { 'host': '127.0.0.1',
               'user': 'myUserid',
               'password': 'myPassword',
               'database': 'myDB' }

    with UseDatabase(config) as cursor:
        _SQL = "select * from log"
        cursor.execute(_SQL)
        data = cursor.fetchall()

"""

import mysql.connector


class UseDatabase:
    def __init__(self, config: dict):
        self.configuration = config

    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
