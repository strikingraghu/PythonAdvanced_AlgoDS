"""

Variable -
A variable is a named location used to store data in the memory.
It is helpful to think of variables as a container that holds data which can be changed later throughout programming.
We don't assign values to the variables, whereas Python gives the reference of the object (value) to the variable.

Constants -
A constant is a type of variable whose value cannot be changed.
It is helpful to think of constants as containers that hold information which cannot be changed later.
Ex - You can think of constant as a bag to store some books and those books cannot be replaced once placed in the bag.

Literals -
Literal is a raw data given in a variable or constant. In Python, there are various types of literals:

Numeric Literals
    Numeric Literals are immutable (unchangeable).
    Numeric literals can belong to 3 different numerical types Integer, Float and Complex.

String Literals
    A string literal is a sequence of characters surrounded by quotes.
    We can use both single, double or triple quotes for a string.
    And, a character literal is a single character surrounded by single or double quotes.

Boolean Literals
    A Boolean literal can have any of the two values: True or False.

Special Literals (None)
    Python contains one special literal i.e. None. We use it to specify to that field that is not created.

Literal Collections -
There are four different literal collections List literals, Tuple literals, Dict literals, and Set literals.

"""

# assigning values
counter = 100
miles = 95.33
name = 'John'

print('Counter =', counter)
print('Miles =', miles)
print('Name =', name)

# multiple assignment

A = B = C = 1
print('A =', A, 'B =', B, 'C =', C)

# numbers
variable_1 = 25
variable_2 = 338.09
variable_3 = 857722
variable_4 = 34.33j

print("Variable A =", variable_1, '|', type(variable_1))
print("Variable B =", variable_2, '|', type(variable_2))
print("Variable C =", variable_3, '|', type(variable_3))
print("Variable D =", variable_4, '|', type(variable_4))
print("--------------------------")
print()

# strings
string_1 = "Hello, are you part of Bengaluru city?"
string_2 = "Indeed, it's a great city!"

# constants (Try to create a constant.py and import this module any python program like constant.PI)
PI = 3.14
GRAVITY = 9.8

# numeric literals

a = 0b1010
b = 100
c = 0o446
d = 0x19b
print('A =', a, '|', 'B =', b, '|', 'C =', c, '|', 'D =', d)

float_1 = 10.5
float_2 = 1.5e2
print('Float 1 =', float_1, '|', 'Float 2 =', float_2)

complex_x = 3.14j
print('X value is =', complex_x, '|', 'Type is =', type(complex_x))

# string literals
strings = 'This is a Python code'
char = 'R'
multiple_line_str = """This is a multi-line comment"""
raw_string = r"raw \n string"
print(strings, '|', char, '|', multiple_line_str, '|', raw_string)

# boolean literals
x = (1 == True)
y = (1 == False)
sample_a = True + 4
sample_b = False + 10
print("Value of sample_a =", sample_a)
print("Value of sample_b =", sample_b)

# special literals
drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)

# literal collections
fruits = ["apple", "mango", "orange"]
numbers = (1, 2, 3)
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}
vowels = {'a', 'e', 'i', 'o', 'u'}

print(fruits, '|', type(fruits))
print(numbers, '|', type(numbers))
print(alphabets, '|', type(alphabets))
print(vowels, '|', type(vowels))
