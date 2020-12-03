# Semoogle

A prototype semantic search engine.

## Quick Overview
In this project, I'll be creating a Semantic Search engine, on a corpus of all Wikipedia texts till 2010. Scalability and the quality of the semantic search are the focus of this project. We find that for single word searches, ontological meaning driven semantic search provides a better understanding, whereas, for phrases and sentences, dense vector-based approaches are better.

## Problem Statement
Traditionally, lexical search has been successfully deployed for indexing and searching keywords amongst billions of unstructured documents, on the web, and otherwise. However, there’s a key problem with this approach, since the user may not necessarily know the exact keyword to search for, or may not be able to use the same words to coherently describe what he’s looking for to the search engine.

Semantic search allows the search to be performed while considering the meaning of what the user is requesting. Overall, this helps improve search accuracy, by using the intent of the user and the overall contextual meaning of the terms being looked for, to generate more relevant knowledge retrieval.

## Building the Index
This process is slightly more complex.
This involves running a FTS5 plugin to build a virtual table in the database.
For all intents and purposes, since we're not using the db for concurrent writes,

## How to run API Server
- cd src/
- export FLASK_APP=main.py
- flask run

## How to reproduce tests in paper
To do this you must have first built your index. Then go to src/ and run python3 sentencembedding_test.py .
