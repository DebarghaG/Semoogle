# Sem-e-lastic

A prototype semantic search engine.

## How to run
'''
cd src/
export FLASK_APP=main.py
flask run
'''

## Building the Index
This process is slightly more complex.
This involves running a FTS5 plugin to build a virtual table in the database.
For all intents and purposes, since we're not using the db for concurrent writes, 
