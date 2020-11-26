from sentence_transformers import SentenceTransformer
import re
from parse import Parser
from vectorizer import Vect
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
import time
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

parsewiki = Parser("../data/WestburyLab.Wikipedia.Corpus.txt")
print("\n\n")
titles = parsewiki.loadTitleVectors()[0:10]
# print(titles)


def most_similar(doc_id, similarity_matrix, matrix):
    print(f'Document: {documents_df.iloc[doc_id]["documents"]}')
    print('\n')
    print('Similar Documents:')
    if matrix == 'Cosine Similarity':
        similar_ix = np.argsort(similarity_matrix[doc_id])[::-1]
    elif matrix == 'Euclidean Distance':
        similar_ix = np.argsort(similarity_matrix[doc_id])
    for ix in similar_ix:
        if ix == doc_id:
            continue
        print('\n')
        print(f'Document: {documents_df.iloc[ix]["documents"]}')
        print(f'{matrix} : {similarity_matrix[doc_id][ix]}')


documents_df = pd.DataFrame(titles, columns=['documents'])
stop_words_l = stopwords.words('english')
documents_df['documents_cleaned'] = documents_df.documents.apply(lambda x: " ".join(re.sub(
    r'[^a-zA-Z]', ' ', w).lower() for w in x.split() if re.sub(r'[^a-zA-Z]', ' ', w).lower() not in stop_words_l))


sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')
start = time.time()
document_embeddings = sbert_model.encode(documents_df['documents_cleaned'])
stop = time.time()
print(stop-start)
print(document_embeddings)
#pairwise_similarities = cosine_similarity(document_embeddings)
#pairwise_differences = euclidean_distances(document_embeddings)
#most_similar(0, pairwise_similarities, 'Cosine Similarity')
#most_similar(0, pairwise_differences, 'Euclidean Distance')



while True:
    query = input("Please enter your search query : ")
    if query == "exit":
        break
    parsewiki.queryIndex(query)
