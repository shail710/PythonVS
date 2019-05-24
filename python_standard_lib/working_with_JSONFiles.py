import json
from pathlib import Path
movies = [
    {'id': 1, 'title': 'Terminator', 'year': 1989},
    {'id': 2, 'title': 'Kindergarten Cop', 'year': 1993}
]
# we pass movies object to json.dumps(). this will format the data as a json object
data = json.dumps(movies)
# print(data)
#Output: [{"id": 1, "title": "Terminator", "year": 1989}, {"id": 2, "title": "Kindergarten Cop", "year": 1993}]

# write to a data file

# data is a simple strin, so we can write it to a file
# Path('movies.json').write_text(data)


# read json

# following line will read all the data from the json file
# data will be a string that includes data formatted as json
data = Path('movies.json').read_text()

# so we will load this data and it will return an array of dictionaries
movies = json.loads(data)
print(movies)
#Output: [{'id': 1, 'title': 'Terminator', 'year': 1989}, {'id': 2, 'title': 'Kindergarten Cop', 'year': 1993}]

# so we can simply get any items in this array
print(movies[0]['title'])
#Output: Terminator
