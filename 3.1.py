# 1. Accept n numbers from
# the user. calculate the sum of all numbers from 1 to n.


print("Count of Numbers ")
no = int(input())
isum= 0
for i in range(0,no):
    print("Enter no : ",i+1)
    temp = int(input())
    isum = isum +temp

print("Sum of",no ,"Numbers is", isum );

