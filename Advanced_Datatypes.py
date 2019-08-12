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
