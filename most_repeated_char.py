from pprint import pprint
sentence = 'This is a common interview questions'

char_map = {}

for char in sentence:
    char_map[char] = char_map.get(char, 0) + 1
pprint(char_map, width=1)

char_map_sorted = sorted(
    char_map.items(),
    key=lambda kv: kv[1],
    reverse=True)

print(char_map_sorted)
