"""
Basic exception Handling 
to handle the error we need to put the statement int he try block
to throw a friendly error we need to puth the exception in the except clause

When Python sees a try block it will execute every statement inthis block,
if any of these statements throw an exception the code in the except clause will eb executed.
If there is no exception, except block will never be executed

else statement is optional. this else block will be executed if no exception is thrown

example:
try:
    age = int(input('Age: '))
except ValueError as exception:
    print('You did not enter a valid age')
    print(exception)
    print(type(exception))
else:
    print('No exception were thrown')
print('Execution continues')

Output:
Age : 2
No exception were thrown
Execution continues

Output:
Age: a
You did not enter a valid age
invalid literal for int() with base 10: 'l'
<class 'ValueError'>
Execution continues

"""
""" ********************************************************************************************************************************************************************** """
"""
Handling different Exceptions

try:
    age = int(input('Age: '))
    xfactor = 10 / age
except ValueError:
    print('You did not enter a valid age')
else:
    print('No exception were thrown')


int he above example, if we pass the age as 0, it will throw an error while executing the xfactor statement
it will not be handled as it will throw different type of error which is ZeroDivisionError

REFER PYTHON3 BUILT IN EXCEPTIONS FOR MORE TYPES OF EXCEPTIONS

so to resolve the issue look at the below block of code

try:
    age = int(input('Age: '))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print('You did not enter a valid age')
else:
    print('No exception were thrown')

Output:
Age: 0
You did not enter a valid age

Output:
Age: 20
No exception were thrown


when python executes the code that we have in try block,
if any of the statement of try block throws an exception and matches with any of the except block,
that except clause will be executed and rest of the except clauses are ignored
"""
""" ********************************************************************************************************************************************************************** """
"""
Cleaning Up

cleaning up means we need to release the external resource once we are done working with them. for example, network/database connections
if we open a file while executing our program, we need to close that file once we are done working with that file

-->In below example, close() will be executed in case of exception
try:
    file = open('exceptions.py')
    age = int(input('Age: '))
    xfactor = 10 / age
    file.close()
except (ValueError, ZeroDivisionError):
    print('You did not enter a valid age')
else:
    print('No exception were thrown')


-->In below example, close() will be executed only if we have an exception
try:
    file = open('exceptions.py')
    age = int(input('Age: '))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print('You did not enter a valid age')
    file.close()
else:
    print('No exception were thrown')


--> to solve the we can duplicate file.close() statement to else block as well.
but duplicating same statement is not a good practice

--> We can use finally clause. finally clause is always executed whether we have an exception or not 

try:
    file = open('exceptions.py')
    age = int(input('Age: '))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print('You did not enter a valid age')
else:
    print('No exception were thrown')
finally:
    file.close()
"""
""" ********************************************************************************************************************************************************************** """
"""
The With Statement

we can achieve the same result as finally with using with statement.
With statement works with objects which supports the context management protocol
python releases the external resources automatically used with with statement

try:
    with open('exceptions.py') as file:
        print('file opened')
    age = int(input('Age: '))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print('You did not enter a valid age')
else:
    print('No exception were thrown')

"""
""" ********************************************************************************************************************************************************************** """
"""
Raise an exception

we can raise an exception in our code

example:

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('Age cannot be 0 or less')
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""
""" ********************************************************************************************************************************************************************** """
"""
Cost of raising Exceptions

Raising exception is not advisable while scalability or performance is a concern

for example:


code1 = """
"""(remove one pair of triple ")
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('Age cannot be 0 or less')
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""
"""

print('first code: ', timeit(code1, number=10000))

Output: first code:  1.997578272


------> Comparision between two different approaches

from timeit import timeit
code1 = """


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('Age cannot be 0 or less')
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """


def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
print('first code: ', timeit(code1, number=10000))
print('second code: ', timeit(code2, number=10000))

Output:
first code:  0.008477232000000001
second code:  0.002522468
"""
