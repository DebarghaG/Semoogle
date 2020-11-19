"""
Checks if the FTS5 is installed for SQLite on your machine.
Pretty straightforwards,
- Returns YES is present
- Returns NO if not present
"""


import sqlite3

con = sqlite3.connect(':memory:')
cur = con.cursor()
cur.execute('pragma compile_options;')
available_pragmas = cur.fetchall()
con.close()

#print(available_pragmas)

if ('ENABLE_FTS5',) in available_pragmas:
    print('YES')
else:
    print('NO')
