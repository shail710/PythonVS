from collections import namedtuple
"""
A class is a blueprint for creating new object
An object is an instance of a class
"""
""" ********************************************************************************************************************************************************************** """
"""
Creating class

example:
class Point:
    def draw(self):
        print('draw')


point = Point()
point.draw()
print(type(point))
print(isinstance(point, Point))

Output:
draw
<class '__main__.Point'>
True
"""
""" ********************************************************************************************************************************************************************** """
"""
Constructors

to pass an argument to a class we need a constructor. constructor is executed when a new object is created

example:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point({self.x}, {self.y})')


point = Point(1, 2)
point.draw()

Output:
Point(1, 2)


The methods we define in a class must have at least one parameter which is called self
Self references to the current object of the class
when calling methods in an object, we never have to supply a value for its parameter, python interpreter does that
"""
""" ********************************************************************************************************************************************************************** """
"""
Class vs Instance Attributes

here in above example, x and y are the instance attributes. they differ from instance to instance.
Similarly, we can have class attributes which we define at the class level and is accessible and same for every instance

in the below example, default color in class attribute

exmaple:
class Point:
    default_color = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point({self.x}, {self.y})')


print(Point.default_color)
point = Point(1, 2)
point.draw()
print(point.default_color)
another = Point(3, 4)
another.draw()
print(another.default_color)

Output:
red
Point(1, 2)
red
Point(3, 4)
red
"""
""" ********************************************************************************************************************************************************************** """
"""
Class vs instance Methods

as we can have class attributes, we can also have class methods.
Class methods are called Factory methods because they return and object

in below example, we have zero as a class method which reurns an object with the initial value of (0, 0)

example:
class Point:
    default_color = 'red'
    # @classmethod is called class decorator. we need to use it before declaring a class method
    @classmethod
    # class method must have atleast one parameter called cls which is a reference to the class itself
    def zero(cls):
        return cls(0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point({self.x}, {self.y})')


point = Point.zero()
point.draw()

Output: Point(0, 0)

"""
""" ********************************************************************************************************************************************************************** """
"""
Magic Methods

REFER PYTHON3 MAGIC METHODS

"""
""" ********************************************************************************************************************************************************************** """
"""
Comparing two Objects
We get False for the beloww comparison of two Objects
because, by default the equalit operator compares the references of the objects
Example:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(1, 2)
other = Point(1, 2)
print(point == other)

Output: False

To solve this problem, we need to use Comparison Magic Methods
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


point = Point(1, 2)
other = Point(1, 2)
print(point == other)

Output: True

But defineing eq magic method doesn't solve the > or < comparison

we need to define them as well

Example:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(10, 20)
other = Point(1, 2)
print(point == other)
print(point > other)
print(point < other)

Output:
False
True
False


we don't need to define gt and lt both.

defining any of them will be good as python will figure out what needs to be done when the opposite operator is executed
"""
""" ********************************************************************************************************************************************************************** """
"""
Performing Arithmetic Operations

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
other = Point(1, 2)
combined = point + other
print(combined.x, combined.y)

Output: 11 22
"""
""" ********************************************************************************************************************************************************************** """
"""
Making custom Containers

refer TagCloudContainer.py in this same folder
"""
""" ********************************************************************************************************************************************************************** """
"""
Private Members

prefixing attributes or methods with '__' makes it private.

However it is accessible with the object._ClassName_AttributeOrMethodname (get it from object.__dict__)
"""
""" ********************************************************************************************************************************************************************** """
"""
Properties

property is an attribute that sits in front of an attribute and allows us to get and set the value of an attribute

so we define a property using inbuilt property() function.
We pass the reference methods to this function as argument.
syntax: property(fget, fset, fdel, doc)
all the parameters are optional

example:
class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative')
        self.__price = value

    price = property(get_price, set_price)


product = Product(10)
print(product.price)
product.price = 20
print(product.price)

Output:
10
20

--> setting property() still gives the access to the methods of the class
One solution is prefix methods with '__'.
but this will make code look ugly.

Class decorators are the alternative to this problem and which will make the code look good
when python interpreter sees @property, it will automatically create a property object
Example:
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative')
        self.__price = value


product = Product(10)
print(product.price)
product.price = 20
print(product.price)

Output:
10
20
"""
""" ********************************************************************************************************************************************************************** """
"""
Inheritance

we can inherit the methods and the attributes of the parent class to the child class.
every class inherits object class
every object is an instance of its own calss and the parent class

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')


class Mammal(Animal):
    def walk(self):
        print('walk')


class Fish(Animal):
    def swim(self):
        print('swim')


m = Mammal()
print(m.age)
m.eat()
m.walk()
print(isinstance(m, Animal))
print(isinstance(m, object))
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))

Output:
1
eat
walk
True
True
True
True
"""
""" ********************************************************************************************************************************************************************** """
"""
Method Overriding

Sometimes we need to define attributes at the parent class level as well as the child class level
see below example:

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')

class Mammal(Animal):
    # following attribute declaration overrides the parent attribute
    def __init__(self):
        self.weight = 2

    def walk(self):
        print('walk')

m = Mammal()
print(m.age)
print(m.weight)


Output:
AttributeError: 'Mammal' object has no attribute 'age'


--> to over come this problem, we use inbuilt super()
super() allows us to access the attributes from the parent class when we have the attributes in the child class well

Example:
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')


class Mammal(Animal):

    def __init__(self):
        # using inbuilt super().Attribute will allow us to access parent attribute
        super().__init__()
        self.weight = 2

    def walk(self):
        print('walk')


class Fish(Animal):
    def swim(self):
        print('swim')


m = Mammal()
print(m.age)
print(m.weight)

Output:
1
2
"""
""" ********************************************************************************************************************************************************************** """
"""
Abstract Base Class

in the good example of inheritance, there are 2 problem

1) we can create an instance of Stream class and can access the methods of Stream Class directly
2)As we have used read method in both the subclass of Stream, we need to remember it to keep the consistency == make a common interface

to solve both of these issue, we have abstract base class abc

the class which has abstract method, we cannot instantiate an object for that class
if any of the class is instantiated with the abstract class and if it does not have abstract method, it throw an error
which means any class derived from abstract class, has to have abstract method else it will consider that class as abstract class

Example:
# we import ABC (Abstract Base Class) class from abc module and also import abstractmethod function to use a decorator




#from abc import ABC, abstractmethod
class InvalidOperationError(Exception):
    pass

# to make Stream an Absract, we need to derive it from ABC


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError('File is already open')
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError('File is already closed')
        self.opened = False

    # Define read method and decorate it with abstractmethod decorator
    # This defines an interface that all the derivative class should follow
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print('Streaming data from a file')


class NetworkStream(Stream):
    def read(self):
        print('Streaming data from network')

# following line of code is an example of an abstract class


# class MemoryStream(Stream):
#     pass

# correct way to create a class which is derived from an abstract class
class MemoryStream(Stream):
    def read(self):
        print('Streaming data from a memory')
"""
""" ********************************************************************************************************************************************************************** """
"""
Polymorphism

polymorphism means many forms.

following example shows that draw function takes many form of object and determines it at a run time

Example:
#from abc import ABC, abstractmethod
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print('TextBox')


class DropdownList(UIControl):
    def draw(self):
        print('DropdownList')

# below function takes an UIControl object as a control and calls the draw mwthod of that class
# We can pass a list or a tuple as an argument and draw funtion will iterate over each item and calls the respective class method


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropdownList()
textbox = TextBox()
draw([ddl, textbox])

Output:
DropdownList
TextBox
"""
""" ********************************************************************************************************************************************************************** """
"""
Duck Typing

Duck typing is a concept that says that the “type” of the object is a matter of concern only at runtime
and you don’t need to to explicitly mention the type of the object before you perform nay kind of operation on that object.
"""
""" ********************************************************************************************************************************************************************** """
"""
Extending Built in Types

class Text(str):
    # we can extend the in built class and define our own method to
    def duplicate(self):
        return self + self


class TrackableList(list):
    # We can extend append method of list base class
    def append(self, object):
        print('Append Called')
        super().append(object)


text = Text('Python')
print(text.duplicate())

list = TrackableList()
list.append(1)

Output:
PythonPython
Append Called
"""
""" ********************************************************************************************************************************************************************** """
"""
Data Classes

when we are dealing with ONLY data or in other words classes have attributes and not the method, we should use namedtuple function
# we import namedtuple function from collections module
from collections import namedtuple
# following line of code will return a tuple with value of x and y which has name Point and type of Point is class
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
# We do not need to define magic method to compare two different objects of the same class
print(p1 == p2)
# since tuple are immutable, we cannot modify the value. we have to create a new object
p1 = Point(x=10, y=20)
# we can access the value with .
print(p1.x, p1.y)

Output:
True
10 20

"""
