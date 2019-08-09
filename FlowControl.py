"""
    Decision making is anticipation of conditions occurring while execution of the program and specifying actions
    taken according to the conditions. Decision structures evaluate multiple expressions which produce TRUE or FALSE as
    an outcome. You need to determine which action to take and which statements to execute if outcome is TRUE or FALSE!
    Types of Decision Making logic -
        Python IF ELSE Statement
        Python IF...ELIF...ELSE Statements
        Python nested IF statements

"""

# if condition

number_1 = 3
if number_1 > 0:
    print(number_1, "is a positive number!")
print("This is always printed")

num = -1
if num > 0:
    print(num, "is a positive number")
print("This is also always printed")

# if else condition

number_2 = -5
if number_2 > 0:
    print("This is a positive number and value entered is {}".format(number_2))
else:
    print("This is a non-positive number and value entered is {}".format(number_2))

# if elif else condition

number_3 = 3.4
if number_3 > 0:
    print("This is a positive number and value entered is {}".format(number_3))
elif number_3 == 0:
    print("You have a zero value!")
else:
    print("This is a negative number and value entered is {}".format(number_3))

# nested loop condition

number_4 = float(input("Enter a number = "))
if number_4 >= 0:
    if number_4 == 0:
        print("Hey, you have entered zero value")
    else:
        print("You have entered a positive number and it's value is {}".format(number_4))
else:
    print("This is a negative number and value entered is {}".format(number_4))
