""" ********************************************************************************************************************************************************************** """
"""
Lists

Lists can contain any type of values
letter = ['a', 'b', 'c']
matrix = [[0, 1], [2, 3]]

we can repeat the same for multiple times in the list with *
zeros = [0] * 5
print(zeros)

Output:[0, 0, 0, 0, 0]

we can combine lists
combined = zeros + letters
print(combined)

Output:[0, 0, 0, 0, 0, 'a', 'b', 'c']

list() creats a new empty list. it accepts iterable arguments. like range()
numbers = list(range(10))
print(numbers)

since string is an also iterable, we can pass string to the list() and list will return the list wilt each chars
chars = list('Hello World')
print(chars)

Output: ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
"""
""" ********************************************************************************************************************************************************************** """
"""
Accessing Lists

Like other languages, we can access the lsit by index
numbers = [1, 2, 3, 4]
print(num[0])

Output: 1

index '-1' will return the first member from the end
print(num[-1])

Otuput: 4

Change the value with the index and also we can print the list using print. we don't need to iterate over list to print it
numbers[0] = 10
print(numbers)

output: [10, 2, 3, 4]

We can slice the list as we do with strings. it returns a new list after slicing it and does not change the original list
print(numbers[0:3])  # does not include the end index
print(numbers)
print(numbers[:2])
print(numbers[2:])
print(numbers[:])

Output:
[1, 2, 3]
[1, 2, 3, 4]
[1, 2]
[3, 4]
[1, 2, 3, 4]

we can pas the third argument as a step. see below example to understand it better
numbers = list(range(20))
print(numbers)
# returns the every 2nd element from the list
print(numbers[::2])
# returns list in reverse order
print(numbers[::-1])
# returns every 2nd element between the index 0 to 11, where 11th index is not included
print(numbers[0:11:2])

Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
[19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
[0, 2, 4, 6, 8, 10]
"""
""" ********************************************************************************************************************************************************************** """
"""
Unpacking Lists

unpacking the lists meant storing a values from a list to another variable.

example:

numbers = [1, 2, 3, 4, 5, 6, 7]
first, second, *other = numbers
print(first)
print(second)
print(other)
print(numbers)

output:
1
2
[3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]

numbers = [1, 2, 3, 4, 5, 6, 7]
first, *other, last = numbers
print(first)
print(other)
print(last)
print(numbers)

output:
1
[2, 3, 4, 5, 6]
7
[1, 2, 3, 4, 5, 6, 7]
"""
""" ********************************************************************************************************************************************************************** """
"""
Looping over lists

For loops can be used to iterate over lists. which will return values
if we need index, we can use enumerate(), this will return an enumerate object which is iterable. in each iteration it will return a tuple
tuple can be upacked as well.
Example:

letters = ['a', 'b', 'c']
# returns each item of the list
for letter in letters:
    print(letter)
# returns tuple after each iteration with index and the item at that index
for letter in enumerate(letters):
    print(letter)
# since tuple is iterable, we can unpack it at the same time
# return the unpacked tuples
for index, letter in enumerate(letters):
    print(index, letter)

Output:
a
b
c
(0, 'a')
(1, 'b')
(2, 'c')
0 a
1 b
2 c

"""
""" ********************************************************************************************************************************************************************** """
"""
Adding or removing items from the lists
letters = ['a', 'b', 'c']
# add at the end of the list
letters.append('d')
print(letters)
# add at specific index
letters.insert(0, '-')
print(letters)
# remover from the end of the list
letters.pop()
print(letters)
# remove from a specific index
letters.pop(0)
print(letters)
# remove with the value. this will remove the first occurance of the item. if there are multiple items with the same value, loop over to remove all
letters.remove('b')
print(letters)

letters.append('b')
letters.append('d')
letters.append('r')
letters.append('s')
print(letters)


# we can remove an item wilt del with index or we can remove the range of items. this is the only diff between pop() and del()
del letters[0:2]
print(letters)

# clear removes all the object int he list
letters.clear()
print(letters)

Output:
['a', 'b', 'c', 'd']
['-', 'a', 'b', 'c', 'd']
['-', 'a', 'b', 'c']
['a', 'b', 'c']
['a', 'c']
['a', 'c', 'b', 'd', 'r', 's']
['b', 'd', 'r', 's']
[]
"""
""" ********************************************************************************************************************************************************************** """
"""
Finding items in lists

if any item is not present in a list, unlike other programming languages, python throws an error

below line of code will throw an error
letters = ['a', 'b', 'c']
print(letters.index('d'))

to prevent this, we can use in operator which return the boolean value
letters = ['a', 'b', 'c']
if 'd' in letters:
    print(letters.index('d'))
else:
    print('Not Present')

Output: Not Present


or else we can use count() too

letters = ['a', 'b', 'c']
if (letters.count('c')) != 0:
    print(letters.index('c'))
if 'd' in letters:
    print(letters.index('d'))
else:
    print('Not Present')

Output:
2
Not Present
"""
""" ********************************************************************************************************************************************************************** """
"""
Sorting Lists
numbers = [3, 51, 2, 8, 6]
# returns sorted list in the ascending order
numbers.sort()
print(numbers)
# returns the list in the descending order
numbers.sort(reverse=True)
print(numbers)

Output:
[2, 3, 6, 8, 51]
[51, 8, 6, 3, 2]


we can use pre-defined sorted() which takes any iterable as an argument and returns a new sorted list

numbers = [3, 51, 2, 8, 6]
# sorts the list in ascending order and returns a new list
print(sorted(numbers))
print(numbers)
# sorts the list in descending order and returns a new list
print(sorted(numbers, reverse=True))
print(numbers)

Output:
[2, 3, 6, 8, 51]
[3, 51, 2, 8, 6]
[51, 8, 6, 3, 2]
[3, 51, 2, 8, 6]


.sort() method cannot sort the list with the tupples.
example:
items = [
    ('product1', 10),
    ('product2', 9),
    ('product3', 12),
]
items.sort()
print(items)

Output: [('product1', 10), ('product2', 9), ('product3', 12)]

to over come this issue, we have to def a function which will take return a number
remember,
we need to pass the reference of the function tot he sort() and NOT to cal the function
also, sort() takes ONLY keywor arguments

Hwere in the below example, we are sorting the list based on the price

example:
items = [
    ('product1', 10),
    ('product2', 9),
    ('product3', 12),
]
def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)

Output: [('product2', 9), ('product1', 10), ('product3', 12)]
"""
""" ********************************************************************************************************************************************************************** """
"""
Lambda functions

In above example of sorting lists with tuples, we needed to define a function which returns a number
Lambda functions are refered as a temp function.
syntax: lambda parameters : expression
we can rewrite the above sorting lists with tuple example code as below

items = items = [
    ('product1', 10),
    ('product2', 9),
    ('product3', 12),
]
items.sort(key=lambda item:item[1])
print(items)

Output: [('product2', 9), ('product1', 10), ('product3', 12)]
"""
""" ********************************************************************************************************************************************************************** """
"""
Map Function

map() executes a specified function over the iterable and returns a map object which is iterable
syntax: map(function, *iterables)

example:

items = items = [
    ('product1', 10),
    ('product2', 9),
    ('product3', 12),
]
# map() will execute the lambda function on each item of the items list
# price = map(lambda item: item[1], items)

# since map() returns an iterable object, we need to iterate over map to get the values
# for item in price:
#     print(item)
# above for loop will generate output as :
# 10
# 9
# 12

# we can convert this map object to a list
prices = list(map(lambda item: item[1], items))
print(prices)

Output: [10, 9, 12]
"""
""" ********************************************************************************************************************************************************************** """
"""
Filter Function

like pre-defined map(), we have filter() in python. it accepts a function and a iterable
filter() executes the function for each item of the iterable and returns an iterable filter object
syntax: filter(function, iterable)

example:
items = [
    ('product1', 10),
    ('product2', 9),
    ('product3', 12),
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

output: [('product1', 10), ('product3', 12)]
"""
""" ********************************************************************************************************************************************************************** """
"""
List Comprehensions

as shown in above examples, we use map() and filter() functions on a list to achieve something
we can achieve the same result using comprehension
comprehension, iterate over an iterable and than applies expression on each item
syntax: [expression for variable in iterable]

example:
items = [
    ('product1', 10),
    ('product2', 9),
    ('product3', 12),
]
# prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]
print(prices)
# filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
print(filtered)

Output:
[10, 9, 12]
[('product1', 10), ('product3', 12)]
"""
""" ********************************************************************************************************************************************************************** """
"""
Zip Function

comprehension can work with 1 list only.
zip() can work with more than one lists. zip() accepts multiple iterables as an argument
since zip() accepts iterables, we can pass a strig or any kind of a iterable to the function
zip() returns an iterable zip object which contains tuples. Each tuple will have values froms all the iterables of the smae index
example:
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip('abc', list1, list2)))

Output: [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
"""
""" ********************************************************************************************************************************************************************** """
"""
Tuples

tuples are like lists.
they are iterable but NOT mutable, means we cannot assign, add, remove items.
It is read only
we can unpack the tuples also
type of a tuple is tuple
"""
""" ********************************************************************************************************************************************************************** """
"""
Swapping variables

with python we can swap the variable easily.
if we want to swap x,y
syntax: x, y = y, x

python it unpacking the values of x, y

x = 10
y = 11

x, y = y, x

print(x, y)

Output: 11 10
"""
""" ********************************************************************************************************************************************************************** """
"""
Arrays

arrays take less memory and perform faster, but this is evident when we are dealing large number of items in list
arrays have all the methods that a list has
the only difference is list can have items of different type bit arrays can't

use arrays when dealing with too large data set otherwise use lists and tuples by default
"""
""" ********************************************************************************************************************************************************************** """
"""
Sets

set is an unordered collection of unique items
we cannot access them with an index since they are unordered
set doesn't carry any duplicates
we can iterate over set.
we can add, remove items from set
we can get the length of the set as well
we can check if the item is present in the set or not using in operator

set is powerful because we can performe Mathametical calculation on it
example:

numbers = [1, 1, 2, 4]
first = set(numbers)
second = {1, 3, 5}

print(first)
# returns a new set that will contain all the unnique items of both sets
print(first | second)
# returns a new with the items that are present in both the sets
print(first & second)
# returns a set with all the different items that are present in first set but not in second
print(first - second)
# returns a set with all the items that are present in either first or second set, but not both this is call symetric difference
print(first ^ second)

output:
{1, 2, 4}
{1, 2, 3, 4, 5}
{1}
{2, 4}
{2, 3, 4, 5}
"""
""" ********************************************************************************************************************************************************************** """
"""
Dictionaries

dictionaries are a collection of a key pair values
initializing dictionary:
point = {} -> empty dictionary
point = {'x':1, 'y':2} -> with values
point = dict() ->Empty dictionary
point = dict(keyword arguments)
    point = dict(x=1, y=2)
in dictionaries, we can only use immutable types as a key, like int, float, complex, string, tuple, frozen set, byte
(mutable objects are list, dict, set, byte array.
a mutable object can change its state or contents and immutable objects cannot.)

since dictionaries are key-pair values, we cannot access values the index. like, point[0]
instead we can use it with key name. like, point['x']
example:
print(point['x'])
Outut: 1

can change the value of key using index. like, point['x'] = 10
can add a value to dictionary. like point['z'] =20

if we pass an invalid key, point['a'], it will give a KeyError.
to avoid this, we have 2 options
1) check for it's existance
    if 'a' in point:
        print(point['a'])
2) use get method
    print(point.get('a')) -> will give None as a output

    we can pass a default value to the key if key does not exist
    print(point.get('a', 0)) -> python will not find key 'a', so it will add the key 'a' with a value 0

delete a key pair using del keyword. like, del point['x']

There are 2 ways of Iterating over a dict
1)   example:
    point = dict(x=1, y=2)

    for key in point:
        print(key)

    Output:
    x
    y

    point = dict(x=1, y=2)

    for key in point:
        print(key, point[key])

    Output:
    x 1
    y 2

2) example:
    point = dict(x=1, y=2)

    for key in point.items():
        print(key)

    Output:
    ('x', 1)
    ('y', 2)

    We can unpack this tuple
    point = dict(x=1, y=2)

    for key, value in point.items():
        print(key, value)

    Output:
    x 1
    y 2
"""
""" ********************************************************************************************************************************************************************** """
"""
Comprehension in dictionary

works exactly like lists comprehension
syntax: {expression for variable in iterable}

values = {key:key * 2 for key in range(5)}
print(values)

Output:
{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
"""
""" ********************************************************************************************************************************************************************** """
"""
Generator Expression

Generator objects are iterable like lists, so we can iterate over generator and in each iteration we generate a new value
There are situations where we might need to work with large data set or potentially an infinite stream of data.
storing this large set of data is not a good idea
So unlike, lists, generators don't store all the values in the memory, they generate a new value in each iteration.

Syntax: syntax: (expression for variable in iterable)
"""
""" ********************************************************************************************************************************************************************** """
"""
Unpakcing Operator

we can use unpacking operator to take out individual values from any iterable.

use * as an unpacking operator for lists, strings
use ** as an unpacking operator for dictionaries

example:
values = [*range(5)]
first = [5, 6, 7]
string = 'Hello'
dictionary = {'x': 1, 'y': 2}
combined = [*values, *first, *string]
print(combined)

Output: [0, 1, 2, 3, 4, 5, 6, 7, 'H', 'e', 'l', 'l', 'o']

first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 3}
combined = {**first, **second}
print(combined)

Output: {'x': 10, 'y': 2, 'z': 3}

notice that if the same key appears in two different dict than it will over ride the value of that key with the latest one

"""
""" ********************************************************************************************************************************************************************** """
