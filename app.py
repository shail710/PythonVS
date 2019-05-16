"""
Python is case sensitive language
Primitive Types in Python:
number
boolen: boolean values need to be capitalized: True False are valid boolean values but not true false
string
"""
""" ********************************************************************************************************************************************************************** """
"""
Strings:
course = "Python Programming"

length of the string
len(course): gives the length of string

returning value at an index
course[0]: gives the first char at the 0th index
course[-1]: index of '-1' in string takes back to the last char of the string and not gives undefined or null.

Slice method
course[0:3]: returns 3 chars starting from the 0th index upto 3rd index. char at index 3 is not included.
course[0:]: returns all the char starting from the starting index, which is 0 in this case, to the end of the string
course[:3]: returns all the chars from the begining upto the endindex which is 3 in this case
course[:]: returns the string itself as we have not passed any start and end index
"""
""" ********************************************************************************************************************************************************************** """
"""
Escape Sequences
if we want to put " in between the string like course = "Python "Programming"
in the above case, python interpreter interprets the second " as the terminator of the string.
# to solve this issue, use \(escape character). course = "Python \"Programming" OR
    use single quotes like : course = 'Python "Programming'
Escape Sequences in python are: 
(use without spaces in between)
dsf \' : includes  in the string
sf \" : includes " in the string
sgs \\ : includes \ int he string
sgs \n : used to print something on new line

"""
""" ********************************************************************************************************************************************************************** """
"""
Formatted Strings
below is the convention to concate the strings
first = 'Shail'
last = 'Shah'
full = first + ' ' + last
print(full)

python has a newer way to concate
first = 'Shail'
last = 'Shah'
full = f'{first} {last}'
print(full)


so here, code between f'' is an expression that we want to be excuted. we can use and valid expression
for example: full = f'{len(first)} {last}' will give the output as 5 Shail
"""

""" ********************************************************************************************************************************************************************** """
"""
String Methods

course = 'Python Programming'

course.upper(): returns a new string and convert it to the upper case. IT DOES NOT AFFECT THE ORIGINAL STRING
course.lower(): returns a new string and convert it to the lower case. IT DOES NOT AFFECT THE ORIGINAL STRING
course.title(): convertes the first character of each word to the upper case
    for example: course = 'python programming'
                print(course.title())
                output: Python Programming
course.strip(): removes the whitespaces from the begining and from the end of the string
    for example: course  = '     Python Programming    '
                print(course.strip())
                output: Python Programming
    course.lstrip(): removes the whitespaces from the begining of the string
    course.rstrip(): removes the whitespaces from the end of the string

course.find(''): returns the index of the passed string
    for example: print(course.find('Pro')) -> returns 7
                print(course.find('pro')) -> returns -1, since python is case sensitive it will not finf string 'pro'

course.replace('',''): replaces a char or a sequence of characters with the new charachters
    for example: print(course.replace('Pr','Jr')) -> returns Python Jrogramming

in operator: returns a boolean if the char or sequence of the characters are present in the string or not.
    for example: print('Pro' in course) -> return true
                print('Pro' not in course) -> returns false
"""

""" ********************************************************************************************************************************************************************** """
"""
Numbers

python supports 3 types of numbers
1) integer = 1
2) float = 1.1
3) complex = 2 + 3j , where j is the imaginary part

Arithmatic operators
print(10 + 3) -> 13
print(10 - 3) -> 7
print(10 * 3) -> 30
print(10 / 3) -> 3.33
print(10 // 3) -> 3, // operator will floor the output into the whole integer
print(10 % 3) -> 1
print(10 ** 3) -> 1000, ** is an exponential operator
"""

""" ********************************************************************************************************************************************************************** """

"""
round() : rounds the floating number
abs(): returns absolute value of the number


Math module:
to use this, import math

refer python3 math module
"""

""" ********************************************************************************************************************************************************************** """

"""
Type Conversion
int(x): converts value to integer
float(x): converts value to float
str(x): converts value to string
bool(x):
    Falsy values in Python:
        ''
        0
        None
    any of the above used with bool() will return False: bool('') -> False
"""
""" ********************************************************************************************************************************************************************** """
"""
Comparision Operators
10 > 3
True

10 >= 3
True

10 < 20
True

10 <= 20
True

10 == 10
True

'10' == 10
False

'10' != 10
True

Comparision Operators can be used with strings as well
"""
""" ********************************************************************************************************************************************************************** """
"""
Conditional Statements:
    syntax:
    if boolean condition:
        code block
    elif boolean condition:
        code block
    else:
        code block
"""
""" ********************************************************************************************************************************************************************** """
"""
Ternary Operator
    syntax:
    variable = return statement1 if boolean condition else return statement2

    example:
    age = 12

    message = 'Eligible' if age >= 18 else 'Not Eligible'
    print(message)
"""
""" ********************************************************************************************************************************************************************** """
"""
Logical operators:
and
or
not

example:
high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print('Eligible')
else:
    print('Not Eligible')
"""
""" ********************************************************************************************************************************************************************** """
"""
Chaining Comparision Operators:

#age should be between 18 and 65

age = 22
if age >= 18 and age < 65:
    print('Eligible')

#we can rewrite the same code block using chainig as below
if 18 <= age < 65:
    print('Eligible')
"""
""" ********************************************************************************************************************************************************************** """
"""
for loops
range() has 3 argumrnts. range(initial val, repeatations, step)
for number in range(1, 10, 2):
    print('Attempt' , number);
Output: Attempt 1
Attempt 3
Attempt 5
Attempt 7
Attempt 9

"""
""" ********************************************************************************************************************************************************************** """
"""
For else loop
In for..else loop, else block will be executed if and only if the for loop is not terminated through the execution
Example:
following block of code will break the for loop after first iteration. Hence, else block will not be executed

successful = True
for number in range(3):
    print('Attempt')
    if successful:
        print('successful')
        break
else:
    print('Attempted 3 times and unsuccessful')

Output: Attempt
successful


following block will never be terminated since the value of successfull will never be True. Hence it will execute else block

successful = False
for number in range(3):
    print('Attempt')
    if successful:
        print('successful')
        break
else:
    print('Attempted 3 times and unsuccessful')

Output: Attemp
Attempt
Attempt
Attempted 3 times and unsuccessful
"""
""" ********************************************************************************************************************************************************************** """
"""
Nested Loops

for x in range(3):
    for y in ranger(3):
        print(f'({x},{y})')

Output:
(0,0)
(0,1)
(0,2)
(1,0)
(1,1)
(1,2)
(2,0)
(2,1)
(2,2)
"""
""" ********************************************************************************************************************************************************************** """
"""
While loop

following command will not terminate when input is QUIT as python is case sensitive
command = ''

while command != 'quit':
    command = input('>')
    print('ECHO', command)


Output:
>shail
ECHO shail
>shah
ECHO shah
>QUIT
ECHO QUIT
>quit
ECHO quit



better way is as following. As python returns a new string when .lower() is used, it won't affect user input

command = ''

while command.lower() != 'quit':
    command = input('>')
    print('ECHO', command)

Output:
>SHAIL
ECHO SHAIL
>FALSE
ECHO FALSE
>QUITE
ECHO QUITE
>QUIT
ECHO QUIT

"""
""" ********************************************************************************************************************************************************************** """
"""
Functions
There should be 2 line breaks between a function and a function call according to PEP8
syntax:
def function_name(parameter_1, parameter_2):
    code block


#calling a function
function_name(argument_1, argument_2)
"""
""" ********************************************************************************************************************************************************************** """
"""
Types of function:
1 - performs task
    example:
    def greet(name):
        print(f'Hi {name}')

2 - returns a value
    example:
    def greet(name):
        return f'Hi {name}'


function by default returns None object which indicates the absence of the value
"""
""" ********************************************************************************************************************************************************************** """
"""
Keyword Arguments

if we want to prefix the argument with the parameter we can. it is called keyword argument.
def increament(number, by):
    return number + by


print(increament(2, by=1))
"""
""" ********************************************************************************************************************************************************************** """
"""

"""
