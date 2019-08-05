"""
If you have ever read 'The Zen of Python' (type "import this" in Python interpreter), the last line states,
Namespaces are one honking great idea -- let's do more of those! So what are these mysterious namespaces?
Let us first look at what name is.
Name (also called identifier) is simply a name given to objects. Everything in Python is an object.
Name is a way to access the underlying object.



"""
a = 5
b = 10
print("ID of variable a =", id(a))
print("ID of variable b =", id(b))
print(id(a) == id(5))
print(id(b) == id(10))