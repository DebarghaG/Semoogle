from flask import Flask
from parse import Parser

app = Flask(__name__)
parsewiki = Parser("../data/WestburyLab.Wikipedia.Corpus.txt")

"""
Uncomment the next line for:
- Parse Baseline Benchmark
- Sequential Search Baseline Benchmark
"""
#parsewiki.parse()
#parsewiki.vanillaQuery("Debargha")

"""
Uncommment the next line to build a search index
Index will be built in SQLite3 for a full text search
"""
#parsewiki.buildIndex()

@app.route('/query/<querystring>')
def query(querystring):
    return(parsewiki.queryIndex("{}".format(querystring)))

#parsewiki.queryIndex("Capitalism is terrible")
#parsewiki.queryIndex("Heart attack symptoms")
#parsewiki.queryTableBM25("Capitalism is terrible")
#parsewiki.queryTableHighlight("Sugar")
