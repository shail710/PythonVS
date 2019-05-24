import sqlite3
import json
from pathlib import Path

#movies = json.loads(Path('movies.json').read_text())
# print(movies)

# with sqlite3.connect('db.sqlite3') as conn:
#     command = 'INSERT INTO Movies VALUES(?,?,?)'
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()

with sqlite3.connect('db.sqlite3') as conn:
    command = 'SELECT * FROM Movies'
    # when we read data from a database we get a cursor object which is iterable
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)
    # after the iteration, we will be at the end of the cursor, so follwing code will return an empty list
    movies = cursor.fetchall()
    print(movies, type(movies))
# Output: [(1, 'Terminator', 1989), (2, 'Kindergarten Cop', 1993)] <class 'list'>
