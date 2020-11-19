"""
Runs SQL Commands with an SQLite3 Database.
This database forms the crux of our index.
"""
import sqlite3


class DBHelper():
    def __init__(self):
        self.conn = sqlite3.connect('../index.db')
        self.c = self.conn.cursor()

    def createTable(self):
        try:
            self.c.execute('''CREATE VIRTUAL TABLE articles USING fts5(id , title , body)''')
            print("INDEX TABLE CREATED")
        except:
            print("Table already existed")

    def insertinTable(self, id, title, body):
        self.c.execute("INSERT INTO articles VALUES (?,?,?)", (id, title, body))
        self.conn.commit()

    def queryTable(self, query):
        self.c.execute("SELECT title FROM articles WHERE body MATCH '%s' ORDER BY RANK" % query)
        return self.c.fetchall()

    def queryTableBM25(self, query):
        self.c.execute("SELECT title FROM articles WHERE body MATCH '%s' ORDER BY bm25(articles)" % query)
        return self.c.fetchall()

    def queryTableHighlight(self, query):
        self.c.execute("SELECT highlight(articles, 2, ' ', '') FROM articles WHERE body MATCH '%s' ORDER BY bm25(articles)" % query)
        return self.c.fetchall()


    def closeConn(self):
        self.conn.close()
