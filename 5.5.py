# 5.      Write a Python program to
# extract characters from various text files and puts them into a list

import glob
ch_list=[]
file_list=glob.glob("*.txt")
for file in file_list:
	with open(file,'r') as f:
		ch_list.append(f.read())
print(ch_list)