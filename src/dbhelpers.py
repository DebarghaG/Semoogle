"""
Runs SQL Commands with an SQLite3 Database.
This database forms the crux of our index.
"""
import sqlite3


class DBHelper():
    def __init__(self):
        self.conn = sqlite3.connect('../index.db')
        self.c = conn.cursor()

    def createTable(self):
        self.c.execute(
            '''CREATE TABLE articles(id real, title text, body text)''')

    def insertinTable(self, id, title, body):
        self.c.execute(
            "INSERT INTO stocks VALUES (1,'First Article','More Text')")
        self.conn.commit()

    def closeConn(self):
        conn.close()
