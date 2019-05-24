import random
import string

# generates the random number
print(random.random())
# generates randon int between given numbers
print(random.randint(1, 10))
# selects random value from the passed array
print(random.choice([1, 2, 3, 4]))
# returns a list of size = k and values from the arrat
print(random.choices([1, 2, 3, 4], k=2))
print(''.join(random.choices('asdfgwe1234!@#$%THJY', k=6)))

print(''.join(random.choices((string.ascii_letters + string.digits), k=6)))


# Output:
# 0.29502670215588533
# 3
# 4
# [1, 2]
# #4fgga
# oIIF6b
