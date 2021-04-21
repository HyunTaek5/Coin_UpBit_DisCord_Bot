import pymysql
from core import get_secret


class DataBase:

    def __init__(self):
        SQL_USER = get_secret("SQL_USER")
        SQL_PASSWORD = get_secret("SQL_PASSWORD")
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  user=SQL_USER,
                                  passwd=SQL_PASSWORD,
                                  db='UpBit',
                                  charset='utf8')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args):
        self.cursor.execute(query, args)

    def execute_one(self, query, args):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def execute_all(self, query, args):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()