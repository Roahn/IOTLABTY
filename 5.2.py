# 2.      Write a Python program to count
# the number of lines in a text file

print("Enter file to open")
filepath = input()
file = open(filepath,"r");
count = 0;

for each in file:
    print(each, end= "")
    count =count +1


print()
print(count)