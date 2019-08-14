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

file_open = open('C:/Users/rathnr/Desktop/Questions.txt')
print("File Details :", file_open)
print("File Contents :", file_open.read())
print("File Size :", file_open.__sizeof__())

