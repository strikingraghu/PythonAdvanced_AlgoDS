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

