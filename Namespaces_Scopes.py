"""

If you have ever read 'The Zen of Python' (type "import this" in Python interpreter), the last line states,
Namespaces are one honking great idea -- let's do more of those! So what are these mysterious namespaces?
Let us first look at what name is.
Name (also called identifier) is simply a name given to objects. Everything in Python is an object.
Name is a way to access the underlying object.

Functions are objects too, so a name can refer to them as well.

In Python, you can imagine a namespace as a mapping of every name, you have defined, to corresponding objects.
Different namespaces can co-exist at a given time but are completely isolated.
A namespace containing all the built-in names is created when a Python interpreter and exists as long we don't exit.
This is the reason that built-in functions like id(), print() etc. are always available to us from any part of code.
Each module creates its own global namespace.
These different namespaces are isolated. Hence, the same name that may exist in different modules do not collide.
Modules can have various functions and classes.
A local namespace is created when a function is called, which has all the names defined in it.
Similar, is the case with class.

"""
a = 5
b = 10
print("ID of variable a =", id(a))
print("ID of variable b =", id(b))
print(id(a) == id(5))
print(id(b) == id(10))
print('-----------------------')
print()

a = 2
print("ID of variable a =", id(a))
print("New value of a =", a)
a = a + 1
print("ID of variable a =", id(a))
print("New value of a =", a)

b = 2
print("ID of variable b =", id(b))
print("New value of b =", b)
print('-----------------------')
print()

# changing a value to a function


def print_hello():
    print("Hello")
a = print_hello()





