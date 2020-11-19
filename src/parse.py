"""
Parses an XML dump of Wikipedia.

"""
import gzip
import time

from dbhelpers import DBHelper


class Parser:
    def __init__(self, dump_location):
        self.dump_location = dump_location
        self.dbobject = DBHelper()


    """
    Method parses the entire contents of the data to be indexed.
    Doesn't store anywhere, mostly supposed to be a  basic baseline benchmark.
    """
    def parse(self):
        print("Reading file from >> " + self.dump_location)
        start = time.time()
        file = open(self.dump_location, 'r')
        article = ""
        articleid = 0
        while True:
            line = file.readline()
            if not line:
                break
            if line == "---END.OF.DOCUMENT---\n":
                # print(articleid)
                articleid += 1
                article = ""
                continue
            article = article + line
        stop = time.time()
        print("Read in " + str(articleid) + " documents")
        print("Took >> " + str(stop - start) + " seconds")

    """
    Sequential reads and find based on the Query
    Worst case performance is bad, just for baseline understanding
    """
    def vanillaQuery(self, query):
        #print("Reading file from >> "+ self.dump_location)
        start = time.time()
        file = open(self.dump_location, 'r')
        article = ""
        articleid = 0
        while True:
            line = file.readline()
            if not line:
                break
            if line == "---END.OF.DOCUMENT---\n":
                articleid += 1
                article = ""
                continue
            article = article + line

            if query in article:
                print(article)
                break

        stop = time.time()

        print("Checked in " + str(articleid) + " documents")
        print("Took >> " + str(stop - start) + " seconds")

    """
    Creates the Index in sqlite3
    """
    def buildIndex(self):
        self.dbobject.createTable()
        start = time.time()
        file = open(self.dump_location, 'r')
        article = ""
        articleid = 0
        while True:
            line = file.readline()
            if not line:
                break
            if line == "---END.OF.DOCUMENT---\n":
                title = article.split("\n")[1]
                articleid += 1
                self.dbobject.insertinTable(articleid, title, article)
                article = ""
                if articleid%10000 == 0:
                    print(articleid)
                continue
            article = article + line

        stop = time.time()


    """
    Query the index
    """
    def queryIndex(self, query):
        start = time.time()
        result = self.dbobject.queryTable(query)
        stop = time.time()
        print("Fetched " + str(len(result)) + " results in "+ str(stop-start) )
