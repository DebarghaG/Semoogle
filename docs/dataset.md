# Westbury Wikipedia Corpus ( 3M+ Documents )
This corpus was created from a snapshot of all the articles in the English part of Wikipedia that was taken in April 2010. It was processed, to remove all links and irrelevant material (navigation text, etc). At the end of the day, the corpus is untagged raw text, which I have then pre-processed such that each article becomes a separate document, and the titles become metadata - for our search engine to use.

The reason for using such a massive corpus of articles was to keep everything I was building up to par with the scalability requirements.

Building a search index out of these 6GB+ raw text files, in itself took about 4 hours on a top of the line i7 10th Gen machine with 16GB RAM. The final index came out to take about 10GB space on the disk.
