"""

Python provides numerous built-in functions that are readily available to us at the Python prompt.
Some of the functions like input() and print() are widely used for standard input and output operations respectively.

"""

# input section

give_num = int(input('Type the number you like in this console! '))
double_check_with_user = (input("Do you want to enter another number? "))

total_sum = 0
give_another_num = 0
total_sum += give_num

while double_check_with_user != 'no':
    give_another_num = int(input('Ok, type another number you like in this console! '))
    if type(give_another_num) == int:
        total_sum += give_another_num
        check_again = (input("Do you still want to enter another number? "))
        if check_again == 'no':
            print(total_sum)
            break

# output section
# (curly braces {} are used as placeholders)
x = 5
y = 10
print("The value of variable x = {} and value of variable y = {}".format(x, y))

# different ways to dump values within placeholders
print("{} city is better than {}".format('Bangalore', 'Bhopal'))
print("{0} city is better than {1}".format('Bangalore', 'Bhopal'))
print("{1} city is better than {0}".format('Bangalore', 'Bhopal'))
