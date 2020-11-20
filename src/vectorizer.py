import warnings
warnings.filterwarnings('ignore')
import gensim
import nltk
nltk.download('brown')
from nltk.corpus import brown

class Vect():
    def __init__(self):
        self.model = gensim.models.Word2Vec(brown.sents())

    """
    Pretty straightforward.
    Most similar vectors are queried and returned
    """
    def closest_three(self, string):
        closest_three = self.model.most_similar(positive=[string], topn = 10)
        return closest_three
