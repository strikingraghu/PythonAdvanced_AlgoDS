""""

Python Keywords – Introduction

This article aims at providing a detailed insight to these keywords.
1. True : This keyword is used to represent a boolean true. If a statement is true, “True” is printed.
2. False : This keyword is used to represent a boolean false. If a statement is false, “False” is printed.
           True and False in python are same as 1 and 0.
3. None : This is a special constant used to denote a null value or a void.
          Its important to remember, 0, any empty container (e.g empty list) do not compute to None.
          It is an object of its own datatype – NoneType.
          It is not possible to create multiple None objects and can assign it to variables.
4. and : This a logical operator in python. “and” Return the first false value .if not found return last.
5. or : This a logical operator in python. “or” Return the first True value.if not found return last.
6. not : This logical operator inverts the truth value.
7. assert : This function is used for debugging purposes. Usually used to check the correctness of code.
            If a statement evaluated to true, nothing happens, but when it is false, “AssertionError” is raised.
8. break : “break” is used to control the flow of loop.
           The statement is used to break out of loop and passes the control to the statement following after loop.
9. continue : “continue” is also used to control the flow of code.
              The keyword skips the current iteration of the loop, but does not end the loop.
10. class : This keyword is used to declare user defined classes.
11. def : This keyword is used to declare user defined functions.
12. if : It is a control statement for decision making. Truth expression forces control to go in “if” statement block.
13. else : It is a control statement for decision making & false expression pushes control to go in “else” block.
14. elif : It is a control statement for decision making. It is short for “else if”.
15. del : del is used to delete a reference to an object. Any variable or list value can be deleted using del.
16. try : This keyword is used for exception handling, used to catch the errors in the code using the keyword except.
          Code in “try” block is checked, if there is any type of error, except block is executed.
17. except : As explained above, this works together with “try” to catch exceptions.
18. raise : Also used for exception handling to explicitly raise exceptions.
19. finally : No matter what is result of the “try” block, block termed “finally” is always executed.
20. for : This keyword is used to control flow and for looping.
21. while : Has a similar working like “for” , used to control flow and for looping.
22. pass : It is the null statement in python. Nothing happens when this is encountered.
23. import : This statement is used to include a particular module into current program.
24. from : Generally used with import, from is used to import particular functionality from the module imported.
25. as : This keyword is used to create the alias for the module imported. i.e giving a new name to the imported module.
26. lambda : This keyword is used to make inline returning functions with no statements allowed internally.
27. return : This keyword is used to return from the function.
28. yield : This keyword is used like return statement but is used to return a generator.
29. with : This keyword is used to wrap the execution of block of code within methods defined by context manager.
30. in : This keyword is used to check if a container contains a value.
         This keyword is also used to loop through the container.
31. is : This keyword is used to test object identity, i.e to check if both objects take same memory location or not.
32. global : This keyword is used to define a variable inside the function to be of a global scope.
33. non-local : This keyword works similar to the global, but rather than global, this keyword declares a
                variable to point to variable of outside enclosing function, in case of nested functions.

"""

# Python code to demonstrate True, False, None, and, or, not!
# showing that None is not equal to 0
# prints False as its false.
print(None == 0)

# showing objective of None
# two None value equated to None
# here x and y both are null
# hence true
x = None
y = None
print(x == y)
print(type(x))

# showing logical operation
# or (returns True)
print(True or False)

# showing logical operation
# and (returns False)
print(False and True)

# showing logical operation
# not (returns False)
print(not True)

# Python code to demonstrate
# del and assert
# initialising list
sample_list = [1, 2, 3, 4, 5]

# print all values for list
print(sample_list)
print("Index value of 4 within list is =", sample_list.index(4))

# using del keyword to delete 3rd element
del sample_list[3]
print("Printing list values after deleting an element =", sample_list)
print('-----------------------')
print()

# demonstrating use of assert
# prints AssertionError
# assert 5 < 3, "5 is not small than 3"

# Python code to demonstrate working of
# in and is
# using 'in' to check
if 's' in 'geeksforgeeks':
    print("Letter 's' is part of the word 'geeksforgeeks'")
else:
    print("Letter 's' is not part of the word 'geeksforgeeks'")

# using 'in' to loop through
for i in 'geeksforgeeks':
    print(i, end=" ")
print("\r")
print('-----------------------')
print()

# Python code to demonstrate working of
# global and non local

# initializing variable globally
sample_var = 10
print("Value of a sample variable =", sample_var)

# used to read the variable
def read():
    print("Generic read function of sample variable =", sample_var)

# changing the value of globally defined variable
def modification1():
    global sample_var
    sample_var = 20

# changing the value of local variable
def modification2():
    sample_var = 30

# reading all values
read()
modification1()
read()
modification2()
read()

# demonstrating non-local
# inner loop changing the value of outer a
# prints 10
print("Value of using a non-local is : ", end="")
def outer():
    a = 5
    def inner():
        nonlocal a
        a = 10
    inner()
    print(a)
outer()

# demonstrating without non local
# inner loop not changing the value of outer a
# prints 5
print("Value of a variable without nonlocal is : ", end="")
def outer():
    a = 5
    def inner():
        a = 10
    inner()
    print(a)
outer()
