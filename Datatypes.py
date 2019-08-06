"""

Every value in Python has a datatype. Since everything is an object in Python programming,
data types are actually classes and variables are instance (object) of these classes.

Python Numbers -
Integers, floating point numbers and complex numbers falls under Python numbers category.
They are defined as int, float and complex class in Python.
Integers can be of any length, it is only limited by the memory available.

Python List -
List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible.
All the items in a list do not need to be of the same type.
Declaring a list is pretty straight forward. Items separated by commas are enclosed within brackets [ ].

"""
# numbers

sample_var1 = 5
print(sample_var1, '|', type(sample_var1))

sample_var2 = 2.00
print(sample_var2, '|', type(sample_var2))

sample_var3 = 1+2j
print(sample_var3, '|', type(sample_var3))
print('-----------------------')
print()

# lists & list slicing

sample_list1 = ['a', 2, 1, 'hello', 44.0]
print(sample_list1)
print("Slicing output =", sample_list1[1:4])
print("Slicing output =", sample_list1[1:])
print("Slicing output =", sample_list1[4:])
print("Slicing output =", sample_list1[:1])
print("Slicing output =", sample_list1[:5])
print('-----------------------')
print()

