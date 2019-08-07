"""

The process of converting the value of one data type to another data type is called type conversion.
Python has two types of type conversion.

Implicit Type Conversion
    In Implicit type conversion, Python automatically converts one data type to another data type.
    This process doesn't need any user involvement.

Explicit Type Conversion
    In Explicit Type Conversion, users convert the data type of an object to required data type.
    We use the predefined functions like int(), float(), str(), etc to perform explicit type conversion

"""
# implicit conversion
num_int1 = 100
num_float1 = 339.2
num_complex1 = 1 + 2j
print("Value(Num + Float) =", num_int1 + num_float1)
print("Overall Value =", num_int1 + num_float1 + num_complex1)

# explicit conversion
num_int2 = 100
num_float2 = 339.2
num_str1 = '100.294'
modified_value = float(num_str1)
print("Converting 'num_str' to float type =", modified_value)
print("Overall Value =", num_int2 + num_float2 + modified_value)
print("Overall Value =", num_int2 + num_float2 + float(num_str1))   # multiple ways to generate same output

"""

Key Points to Remember:
    Type Conversion is the conversion of object from one data type to another data type.
    Implicit Type Conversion is automatically performed by the Python interpreter.
    Python avoids the loss of data in Implicit Type Conversion.
    Explicit Conversion is also called Type Casting, the data types of object are converted using predefined function.
    In Type Casting loss of data may occur as we enforce the object to specific data type.

"""

