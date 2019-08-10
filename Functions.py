"""

    In Python, function is a group of related statements that perform a specific task.
    Functions help break our program into smaller and modular chunks.
    As our program grows larger and larger, functions make it more organized and manageable.
    Furthermore, it avoids repetition and makes code reusable.

"""


def odd_or_even(give_an_input):
    if give_an_input % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

odd_or_even(6778)
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
