from parse import Parser

if __name__ == '__main__':
    parsewiki = Parser("../data/WestburyLab.Wikipedia.Corpus.txt")
    #parsewiki.parse()
    #parsewiki.vanillaQuery("Debargha")
    #parsewiki.buildIndex()
    parsewiki.queryIndex("Capitalism is terrible")
    parsewiki.queryIndex("Heart attack symptoms")
    parsewiki.queryTableBM25("Capitalism is terrible")
    parsewiki.queryTableHighlight("Sugar")
