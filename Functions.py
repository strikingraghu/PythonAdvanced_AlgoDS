"""

    In Python, function is a group of related statements that perform a specific task.
    Functions help break our program into smaller and modular chunks.
    As our program grows larger and larger, functions make it more organized and manageable.
    Furthermore, it avoids repetition and makes code reusable.

"""


def odd_or_even(give_an_input):
    """
    Sample function that takes an input
    from an end user

    """
    if give_an_input % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

odd_or_even(6778)
print(odd_or_even.__doc__)
print("--------------------------")


def greet_person(name):
    if type(name) is str:
        print("Hello", name)
        print("Have a great day ahead!")
    else:
        print(name, " = Name should be a string value & not any other type!")

greet_person("Ramesh")  # Calling greet_person function with String value
greet_person(32)  # Calling greet_person function with Integer value

print("--------------------------")


def wishing_person(name, message='Good Luck!'):
    print('Hello', name)
    print(message)

wishing_person("Sam")
print("--------------------------")


def fun():
    string_val = "GeeksforGeeks"
    some_num = 20
    return string_val, some_num

string_val, some_num = fun()
print(string_val)
print(some_num)
print("Close of fun() function!")


def absolute_value(num):
    """
    This function provides an absolute value
    of the entered number
    """
    if num > 0:
        return num
    else:
        return -num

print(absolute_value(2))
print(absolute_value(-5))
print(absolute_value.__doc__)
print("--------------------------")


def calc_factorial(num):
    if num == 1:
        return 1
    else:
        return num * calc_factorial(num-1)

num = 8
print("The factorial of", num, "is", calc_factorial(num))


# lambda
double = lambda x: x * 2
print("Output of Lambda function -", double(5))

my_list_sample = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x % 2 == 0), my_list_sample))
print("Output of Lambda function -", new_list)

another_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
get_new_list = list(map(lambda x: x * 2, another_list))
print("Output of Lambda function -", get_new_list)
print("--------------------------")


# global functions
var_c = 1
def add_func():
    # var_c = var_c + 2     # UnboundLocalError will be noticed for this function. Commented -
    print(var_c)
add_func()


def add_another_func():
    global var_c
    var_c = var_c + 2
    print("Inside add_another_func(): ", var_c)

add_another_func()
print("In main function: ", var_c)

# global nested function


def sample_foo():
    var_x = 20

    def sample_bar():
        global var_x
        var_x = 25
    print("Before calling sample_bar() : ", var_x)
    print("Calling sample_bar() now -")
    sample_bar()
    print("After calling sample_bar() : ", var_x)

sample_foo()
print("X's value in main function: ", var_x)
# If we make any changes inside the bar() function, the changes appears outside the local scope, i.e. foo().
# Before and after calling bar(), the variable x takes the value of local variable i.e x = 20.
# Outside of the foo() function, the variable x will take value defined in the bar() function i.e x = 25.
print("--------------------------")
