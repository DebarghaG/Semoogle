"""
Parses an XML dump of Wikipedia.

"""
import gzip
import time

from dbhelpers import DBHelper


class Parser:
    def __init__(self, dump_location):
        self.dump_location = dump_location

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
