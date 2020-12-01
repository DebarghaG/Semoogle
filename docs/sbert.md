# Thesaurus as Ontological Dictionary
PyDictionary is a Dictionary Module for Python 2/3 to get meanings, translations, synonyms and Antonyms of words. It uses a mining-based approach using BeautifulSoup, whereby Princeton’s WordNet is used for getting the lexical meanings, and synonym.com for obtaining synonyms.

# Sentence Embeddings using Siamese BERT-Networks
### Frameworks used: PyTorch, Spacy and HuggingFace.

Sentence-BERT (SBERT) is a modification of the pre-trained BERT network to use siamese and triplet network structures to derive semantically meaningful sentence embeddings that can be compared using cosine-similarity.  What attracted me to this paper was that it clearly says that this approach allows usage in large scale applications like semantic similarity comparisons, and information retrieval using semantic search.

The pre-trained model that was used for this paper, has been demonstrated to achieve state of the art results on the Semantic Textual Similarity ( STS ) tasks, at the time of its publication.

Relevant quotes from the paper
Finding the most similar pair in a collection of 10,000 sentences requires about 50 million inference computations (~65 hours) with BERT.  This reduces the effort for finding the most similar pair from 65 hours with BERT / RoBERTa to about 5 seconds with SBERT, while maintaining the accuracy from BERT.
SBERT fine-tunes BERT in a siamese / triplet network architecture. We evaluated the quality on various common benchmarks, where it could achieve a significant improvement over state-of-the-art sentence embeddings methods.


## Why Transformers and BERT?
Google’s paper introducing BERT is considered an inflection point in the quest for better models in natural language processing. In general, Recurrent Neural Networks provided the best results with NLP tasks, because they had contextual sequential importance, i.e. weights must be assigned based on not just the most recent word, but also the previous ones. Transformers essentially made sure that sequential data didn’t have to be processed in order. ( RNN’s required it, and was a bottleneck to it’s performance ). Therefore, Transformers can be trained on much larger corpuses of data, with better performance.

BERT’s Transformer therefore is a type of attention mechanism that allows it to learn contextual relationships between words in documents. The Transformer contains an encoder that reads the text input and a decoder that produces a prediction for the given task. The encoder mechanism is the most important bit, since we’re generating a language model.

Most language models use textual inputs sequentially, i.e. from left to right. The transformer reads the entire text sequence all at the same time. Therefore, it’s bidirectional. This is great because the model then understands the context of a word based on all of its surroundings, whether on the left or the right. A lot more can be written about BERT’s mechanism, especially around MLM masks, and fine tuning, but that’s not the subject of this paper.

## What’s new about SentenceBERT
Simple approaches such as averaging BERT embeddings of the different words in a sentence, to create the sentence embeddings - although provides us with fixed length embedding for a given phrase or sentence, doesn’t perform well on Semantic Textual Similarity (STS) tasks. We therefore need more sophisticated approaches, to finetune BERT.

SentenceBERT was made specifically for semantic similarity tasks, therefore it’s task is to derive semantically meaningful sentence embeddings. It adds a pooling operation, which is essentially the equivalent of sliding a filter over the feature map so that a summarization of the features is covered by the filter. It uses a siamese and triplet network to finetune the BERT model, such that it generates semantically meaningful embeddings.
The model uses mean squared error loss as the objective function, and a triplet objective function - where for an anchor sentence a, positive sentence p, and negative sentence n - we minimize for the following loss function. ( Trained over datasets that have semantic sentences grouped )

I’ve been through the paper in a lot of detail, and the experiments are explained very well over there. It would make no sense to repeat every little detail inside the paper here, therefore, I’m glossing over a lot of details.
