#File Size of the file

import os
print("Enter file to open")
filepath = input()
file = open(filepath)
 

file.seek(0, os.SEEK_END)
 
print("Size of file is :", file.tell(), "bytes")