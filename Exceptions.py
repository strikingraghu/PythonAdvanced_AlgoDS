"""

Python provides two very important features to handle any unexpected error in your Python programs
and to add debugging capabilities! Exception Handling − This would be covered in this script.
    a) Exception Handling/Standard Exceptions.
    b) Assertions.

"""
import sys
import os


random_list = ['a', 'e', 'i', 'o', 'u', 1, 2, 3, 4, 5]
for each_element in random_list:
    try:
        print("The element is :", each_element)
        if each_element % 2 == 0:
            print("Element divisible by 2")
        else:
            print("Not an integer or numeric value not divisible by 2")
    except TypeError:
        print("Oops!", sys.exc_info()[0], "occured.")
        print("Next Entry")
        print()
print("Done with all steps!")
print('-----------------------')

# io error

try:
    file_handling = open("txt")  # To test this script, give a wrong file name. You can see exception!
    file_handling.write("Modified via Script implemented for Python exceptions!")
except IOError:
    print("Error: Can't read the or locate the file/file path")
else:
    print("Modifications are applied to this Python file, check the same")
    file_handling.close()
print('-----------------------')


# file not found error

try:
    file_handling = open("txt")  # To test this script, give a wrong file name. You can see exception!
    file_handling.write("Modified via Script implemented for Python exceptions!")

except (IOError, FileNotFoundError):
    print("Error: Can't read the or locate the file/file path. FileNotFoundError")

else:
    print("Modifications are applied to this Python file, check the same")
    file_handling.close()
print('-----------------------')


# zero division error

one_input = int(input("Enter one number "))
two_input = int(input("Enter one more number "))
while True:
    try:
        print("{0} / {1} is {2}".format(one_input, two_input, one_input/two_input))
        break
    except ZeroDivisionError:
        print("Can't divide via Zero")
        one_input = int(input("Enter one number "))
        two_input = int(input("Enter one more number "))
print("ZeroDivisionError logic is done")
print('-----------------------')

# runtime error

try:
    os.mkdir(":\\python_exception")
    print("New Directory Created")
    print(sys.copyright)
except (RuntimeError, OSError, SystemError):
    print("Exception noticed for OS module")
print("Done with Runtime Error logic!")
print('-----------------------')

# index error
sample_list = ['Ram', 'Sita', 'Hanuman', 'Lakshman', 100, 200, 300, 400]
print("Length :", sample_list.__len__())
try:
    print("Trying to print Index value that is not present :", sample_list[10])
    raise IndexError
except IndexError as IE:
    print("Index Error is noticed for this one : ", IE.__doc__, IE.__class__, IE)
print("Done with Index Error logic")
print('-----------------------')


# user defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when an input is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when an input is too large"""
    pass

number_sample = 10
while True:
    try:
        given_number = int(input("Enter one number"))
        if given_number < number_sample:
            raise ValueTooSmallError
        elif given_number > number_sample:
            raise ValueTooLargeError
    except ValueTooSmallError:
        print("This is small value")
        print()
    except ValueTooLargeError:
        print("This is a large value")
        print()
    finally:
        if given_number == number_sample:
            print("Congrats, you have entered a right number")
            break
    print("All steps are performed!")
