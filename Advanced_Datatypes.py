"""

Refer to Datatypes script for Dictionary definitions -

"""

# numbers
import decimal
import math
import random

var_int = 5
print("Type Conversion - Int - Float :", float(var_int))

var_decimal = 0.1
print("Output of Decimal :", var_decimal)
print("Output of Decimal :", decimal.Decimal(var_decimal))

# math module
print("Math Module :", math.pi)
print("Math Module :", math.cos(math.pi))

# Output: 22026.465794806718
print(math.exp(10))

# Output: 3.0
print(math.log10(1000))

# Output: 1.1752011936438014
print(math.sinh(1))

# Output: 720
print(math.factorial(6))

var_x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("Random Output :", random.choice(var_x))
print('-----------------------')

# lists
sample_list1 = ["Happy", [2, 0, 1, 5]]
print("List Output :", sample_list1)
print("List Output :", sample_list1.__len__())
print("List Output :", sample_list1[1][3])  # Iterating on 2nd element within this list and picking index [3] element

sample_list2 = [2, 4, 98, 283, 192, 99, 13, 587, 539, 987]
print("Negative Indexing List Output :", sample_list2[-4])
print("List Output :", sample_list2[1:4])
sample_list2.extend([1000, 2000, 3000])
print("Extended List Output :", sample_list2)
del sample_list2[4:5]
print("After Deleting Element List Output :", sample_list2)
sample_list2.pop()
print("After Pop() Call :", sample_list2)
print('-----------------------')


# tuples

