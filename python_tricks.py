# Simple comma, be this guy:

names = [
    'Alice',
    'Bob',
    'Dilbert',
]

# Not this guy:
names = [
    'Alice',
    'Bob',
    'Dilbert'
]

# When reviewing changes you'll be thankful


# Use of assertions

TEST_PRODUCT = {'price': 1000, 'name': 'book'}


def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price'], f'The discount is not correct: {discount}.'
    return price


# Assertion won't raise since it considers it a tuple
assert (1 == 2, 'This should fail')


# Context managers
with open('hello.txt', 'w') as f:
    f.write('Hello world!')


# Internally it is equivalent to:
f = open('hello.txt', 'w')
try:
    f.write('Hello world!')
finally:
    f.close()


# Write your own:
class ManagedFile:
    def __init__(self, name):
        self._name = name
        self.file = None

    def __enter__(self):
        self.file = open(self._name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with ManagedFile('hello.txt') as f:
    f.write('Hello world!')

"""
_var        # Internal/private use. Either method attribute or method
var_        # Name equal to reserved word, for instance: 'class_'
__var       # Avoids naming conflict in subclasses.
__var__     # Special use: __init__, __exit__, __str__, ...
_           # Temporary on insignificant variable
"""


class MyClass():
    def __init__(self, class_, subclass):
        self._class = class_
        self._subclass = subclass

    def count(self):
        for _ in range(10):
            self._my_print()

    def _my_print(self):
        print(f'{self._class}.{self._subclass}: Hello world!')

name = 'Bob'
# String formatting

# 1. "Old style"
'Hello, %s' % name

# 2. "New style"
'Hello, {}'.format(name)
'Hello, {name}'.format(name=name)

# 3. Literal string interpolation (Python 3.6+)
f'Hello, {name}!'

# 4. Template strings
from string import Template
t = Template('Hey, $name!')
t.substitute(name=name)

# Functions


# Functions are objects
def yell(text):
    return text.upper() + '!'

yell('hello')
> 'HELLO!'

bark = yell
bark('woof')
> 'WOOF!'

bark.__name__
> 'yell'

# Functions can be stored in data structures.
funcs = [bark, str.lower, str.capitalize]
for f in functs:
    print(f('hey'))
> 'HEY!'
> 'hey'
> 'Hey'

# Functions can be passed to other functions!
def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)

greet(bark)
> 'HI, I AM A PYTHON PROGRAM!'



# Functions can be nested.
def speak(text):
    def whisper(t):
        return t.lower() + '...'

    return whisper(text)


# Functions can capture local state.
def make_adder(n):
    def add(x):
        return x + n
    return add


plus_3 = make_adder(3)
plus_5 = make_adder(5)

plus_3(4)
> 7
plus_4(4)
> 9


# Objects can behave like functions.
class Adder():
    def __init__(self, n):
        self._n = n

    def __call__(self, x):
        return self._n + x


plus_3 = Adder(3)
plus_3(4)
> 7


# Lambdas
add = lambda x, y: x + y
add(5, 3)
> 8


(lambda x, y: x + y)(5, 3)
> 8

# Real use
tuples = [
    (1, 'd'),
    (2, 'b'),
    (4, 'a'),
    (3, 'c'),
]

sorted(tuples, key=lambda x: x[1])
[(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]

# Harmful
list(filter(lambda x: x % 2 == 0, range(16)))

# Better
[x for x in range(16) if x % 2 == 0]



# Decorators
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper

@uppercase
def greet():
    return 'Hello!'

greet()
> 'HELLO!'



def strong(func):
    def wrapper()
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper()
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
def greet():
    return 'Hello!'

greet('Hello!')
> '<strong><em>Hello!</em></strong>'





def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper



def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

foo()
> TypeError:
> foo() missing 1 required positional arg: 'required'

foo('hello')
> 'hello'

foo('hello', 1, 2, 3)
> 'hello'
> (1, 2, 3)

foo('hello', 1, 2, 3, key1='value', key2=999)
> 'hello'
> (1, 2, 3)
> {'key1': 'value', 'key2': 999}



# Argument unpacking

def print_vector(x, y, z):
    print(f'<{x}, {y}, {z}>')

print_vector(0, 1, 0)
tuple_vec = (1, 0, 1)
list_vec = [1, 0, 1]

print_vector(
    tuple_vec[0],
    tuple_vec[1],
    tuple_vec[2],
)
> '<1, 0, 1>'

print_vector(*tuple_vec)
> '<1, 0, 1>'

print_vector(*list_vec)
> '<1, 0, 1>'


# "is" vs "=="

a = [1, 2, 3]
b = a

a == b
> True
a is b
> True

c = list(a)
a == c
> True
a is c
> False


# repr and str

class Car:
    def __init__(self, color, km):
        self._color = color
        self._km = km

    def __str__(self):
        return f'{self._color} car with {self._km} km.'

    def __repr__(self):
        return f'Car({self._color}, {self._km})'


my_car = Car('red', 1000)
str(my_car)
> 'red car with 1000 km.'
repr(my_car)
> 'Car(red, 1000)'

# Exceptions

def validate(name):
    if len(name) < 10:
        raise ValueError(f'Name too short: {name}')

validate('joe')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in validate
ValueError

class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)

validate('joe')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in validate
NameTooShortError: joe


# Cloning

new_list = list(original_list)
new_dict = dict(original_dict)
new_set = set(original_set)

original = [[1, 2, 3], [4, 5, 5]]
copy = list(original)
copy.append('test')

copy
> [[1, 2, 3], [4, 5, 5], 'test']
original
> [[1, 2, 3], [4, 5, 5]]

copy[0][0] = 'X'
copy
> [['X', 2, 3], [4, 5, 5], 'test']
original
> [['X', 2, 3], [4, 5, 5]]

# Cloning part 2

import copy

original = [[1, 2, 3], [4, 5, 5]]
copy_shallow = copy.copy(original)
copy_deep = copy.deepcopy(original)

copy_shallow.append('test')
original
> [[1, 2, 3], [4, 5, 5]]
copy_shallow
> [[1, 2, 3], [4, 5, 5], 'test']
copy_deep
> [[1, 2, 3], [4, 5, 5]]

copy_shallow[0][0] = 'X'
copy_shallow
> [['X', 2, 3], [4, 5, 5], 'test']
original
> [['X', 2, 3], [4, 5, 5]]
copy_deep
> [[1, 2, 3], [4, 5, 5]]

copy_deep[0][0] = 'Y'
copy_deep
> [['Y', 2, 3], [4, 5, 5]]
copy_shallow
> [['X', 2, 3], [4, 5, 5], 'test']
original
> [['X', 2, 3], [4, 5, 5]]



# Abstract classes


class Base:
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()

class Concrete(Base):
    def foo(self):
        return 'foo() called'

    # We forgot to implement bar :O!

c = Concrete()
c.foo()
> 'foo() called'
c.bar()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in bar
NotImplementedError



import abc

class Base(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def foo(self):
        pass

    @abc.abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass

    # We forgot to implement bar, again :/

b = Base()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class Base with abstract methods bar, foo

c = Concrete()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class Concrete with abstract methods bar

