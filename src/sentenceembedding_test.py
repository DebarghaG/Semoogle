from sentence_transformers import SentenceTransformer
import re
from parse import Parser
from vectorizer import Vect
from scipy.spatial.distance import cosine
from sklearn.metrics.pairwise import euclidean_distances
import time
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import nltk
from PyDictionary import PyDictionary
dictionary = PyDictionary()

nltk.download('stopwords')

parsewiki = Parser("../data/WestburyLab.Wikipedia.Corpus.txt")
print("\n\n")
# Just over the first 10,000 documents
titles = parsewiki.loadTitleVectors()[0:10000]
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
#print(stop - start)
#print(document_embeddings)
#pairwise_similarities = cosine_similarity(document_embeddings)
#pairwise_differences = euclidean_distances(document_embeddings)
#most_similar(0, pairwise_similarities, 'Cosine Similarity')
#most_similar(0, pairwise_differences, 'Euclidean Distance')

while True:
    query = input("Please enter your search query : ")
    query_embedding = sbert_model.encode(query)
    maxcosineSimilarity = 0
    document_id = 0
    docfoundat = 0
    # print(query_embedding)

    print("\n\nOntologically approaching the problem:")
    print(dictionary.synonym(query))

    print("\n\nApproaching the problem with a SentenceTransformer :")

    cohesive_titles = []
    similarity_scores = []

    for i in document_embeddings:
        sim = 1 - (cosine(query_embedding, i))
        # print(sim)
        cohesive_titles.append(titles[document_id])
        similarity_scores.append(sim)
        if sim > maxcosineSimilarity:
            maxcosineSimilarity = sim
            docfoundat = document_id
        document_id = document_id + 1

    """
    print("Most semantically similar to :")
    print(maxcosineSimilarity)
    print(titles[docfoundat])
    print("\n")
    """

    print("You might be looking for :")
    list1, list2 = (list(t)
    for t in zip(*sorted(zip(similarity_scores, titles), reverse=True)))
    print(list2[:10])
    print("\n")

    if query == "exit":
        break
    parsewiki.queryIndex(query)
