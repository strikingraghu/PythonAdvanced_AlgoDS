"""

Python provides two very important features to handle any unexpected error in your Python programs
and to add debugging capabilities! Exception Handling − This would be covered in this script.
    a) Exception Handling/Standard Exceptions.
    b) Assertions.

"""
import sys


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


# zerodivisionerror

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
