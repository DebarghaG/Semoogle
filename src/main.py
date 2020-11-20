from flask import Flask
from parse import Parser
from vectorizer import Vect

app = Flask(__name__)
parsewiki = Parser("../data/WestburyLab.Wikipedia.Corpus.txt")

vectorCreator = Vect()
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
    """
    - Use words in search query that are not stopwords
        - Replace those words with synonyms
        - Replace those words with the Word2Vec embeddings
        - Replace those words with the BERT embeddings
        - Replace those words with the AlBERT embeddings
    - Use the augmented strings to run the search
    """

    closest = []
    try:
        closest = vectorCreator.closest_three(querystring)
    except:
        print("Word not in vocabulary")


    return(parsewiki.queryIndex("{}".format(querystring)))

#parsewiki.queryIndex("Capitalism is terrible")
#parsewiki.queryIndex("Heart attack symptoms")
#parsewiki.queryTableBM25("Capitalism is terrible")
#parsewiki.queryTableHighlight("Sugar")
