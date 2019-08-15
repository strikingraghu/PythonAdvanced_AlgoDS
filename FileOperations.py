"""

File is a named location on disk to store related information.
It is used to permanently store data in a non-volatile memory (e.g. hard disk).
Since, random access memory (RAM) is volatile which loses its data when computer is turned off,
we use files for future use of the data. When we want to read from or write to a file we need to open it first.
When we are done, it needs to be closed, so that resources that are tied with the file are freed.

Hence, in Python, a file operation takes place in the following order.
Open a file
Read or write (perform operation)
Close the file

"""

file_operations = open('C:/Users/rathnr/Desktop/Questions.txt')
print("File Details :", file_operations)
print("File Contents :", file_operations.read())
print("File Size :", file_operations.__sizeof__())
print("Closing File :", file_operations.close())

# write
file_activities = open('C:/Users/rathnr/PycharmProjects/PythonBasicAdvanced/file_activities.txt',
                       encoding='utf-8', mode='w')
file_activities.write('Python is the best programming language!\n')
file_activities.write('Java is the best programming language!\n')
file_activities.write('JS is the best programming language!\n')
file_activities.write('.Net is the best programming language!\n')
file_activities.write('PHP is the best programming language!\n')
file_activities.write('Node is the best programming language!\n')
file_activities.close()
file_activities = open('C:/Users/rathnr/PycharmProjects/PythonBasicAdvanced/file_activities.txt')
print("Another Way - Reading Specific Line: ", file_activities.readlines())
file_activities.close()
