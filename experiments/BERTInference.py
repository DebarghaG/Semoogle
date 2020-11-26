from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances

import torch

import time as time
start = time.time()
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained("bert-base-uncased")


stop = time.time()

print(stop-start)
text1 = "Hello my name is Debargha"
start = time.time()
encoded_input1 = tokenizer(text1, return_tensors='pt')
output1 = model(**encoded_input1)


text2 = "Hello my name is Sanchita"
start = time.time()
encoded_input2 = tokenizer(text2, return_tensors='pt')
output2 = model(**encoded_input2)

stop = time.time()
#print(euclidean_distances(output1[0].detach(), output2[0].detach()))

print(output2.logits)
print(stop-start)



print(output1[1])
#print(output2)
