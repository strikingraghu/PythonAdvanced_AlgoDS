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
# numbers (Immutable)

sample_var1 = 5
print(sample_var1, '|', type(sample_var1))
print(id(sample_var1))
sample_var1 = 11
print(id(sample_var1))

sample_var2 = 2.00
print(sample_var2, '|', type(sample_var2))

sample_var3 = 1+2j
print(sample_var3, '|', type(sample_var3))
print('-----------------------')
print()

# lists & list slicing (Mutable/Ordered/Duplicates Allowed)

sample_list1 = ['a', 2, 1, 2, 1, 'hello', 44.0]
sample_list2 = [1, 99, 100, 2, 2, 39, 4, 4, 83]
print("List Output =", sample_list1)
print("List Output =", sample_list2)
print(sample_list1[3], '|', id(sample_list1[3]))
print("Slicing output =", sample_list1[1:4])
print("Slicing output =", sample_list1[1:])
print("Slicing output =", sample_list1[4:])
print("Slicing output =", sample_list1[:1])
print("Slicing output =", sample_list1[:5])
sample_list1[3] = 0b101011001110  # inserting/modifying one element
print(sample_list1[3], '|', id(sample_list1[3]))
print(sample_list1)
print('-----------------------')
print()

# tuple (Immutable/Ordered/Duplicates Allowed)
sample_tuple1 = (1, 1, 2, 236, 8, 8, 3, 3)
print("Tuple Output =", sample_tuple1)
for id_value in sample_tuple1:
    print("ID =", id(id_value))

print(sample_tuple1[1])
# sample_tuple1[1] = 10 # We can't change value
print(sample_tuple1)
print('-----------------------')
print()

# strings (Immutable)
sample_string1 = 'Hello World'
sample_string2 = 'Hello Bangalore'
print("Printing String1 =", sample_string1)
print("Printing String2 =", sample_string2)
print(sample_string1[0], '|', id(sample_string1[0]))
print(sample_string1[1], '|', id(sample_string1[1]))
for id_value_str in sample_string1[:]:
    print("ID =", id(id_value_str), '|', "Value =", id_value_str)
print('-----------------------')
print()

# set (Unordered & Unique)
sample_set1 = {1, 4, 'hello', 8, 1, 2, 2}
print('Set Output =', sample_set1)
sample_set2 = {4, 4, 1, 1, 1, 3928, 3, 9, 00, 0, 282}
sample_set3 = {'a', 'x', 'y', 'b', 'c'}
print(sample_set2)
print(sample_set3)
for id_set_val in sample_set2:
    print("ID =", id(id_set_val), '|', "Value =", id_set_val)
print(len(sample_set2))
print('-----------------------')
print()

# dictionary (Unordered & Allows Duplicates)
sample_dict1 = {1: 2, 2: 3, 3: 4, 4: 5, 5: 2, 6: 3, 7: 4, 8: 5}
print("Dictionary Output =", sample_dict1)
print("Dictionary Keys Only =", sample_dict1.keys())    # key is always unique
print("Dictionary Values Only =", sample_dict1.values())

