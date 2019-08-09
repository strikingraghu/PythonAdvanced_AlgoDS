"""

    In general, statements are executed sequentially.
    The first statement in a function is executed first, followed by the second, and so on.
    There may be a situation when you need to execute a block of code several number of times.
    Programming languages provide various control structures that allow for more complicated execution paths.
    Loop Type & Description
        WHILE LOOP
            Repeats a statement or group of statements while a given condition is TRUE.
            It tests the condition before executing the loop body.
        FOR LOOP
            Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.
        NESTED LOOP
            You can use one or more loop inside any another while loop, for loop or do..while loop.

"""

# for loop

total_sum = 0
sample_num = [3, 6, 9, 12, 15, 18]
for calc_all in sample_num:
    total_sum += total_sum + calc_all
print("Value of the numbers in the list is =", total_sum)

# for loop

for number_range in range(10, 21):
    for i in range(2, number_range):
        if number_range % i == 0:
            j = number_range / i
            print('%d equals %d * %d' % (number_range, i, j))
            break
    else:
        print(number_range, 'is a prime number')
