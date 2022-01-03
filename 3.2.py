
# 2. Accept n number from user
# and print it's multiplication table.


no = int(input())
for j in range(1,no+1):
    h =int(input())
    j=h
    print("Table of ",j)
    for i in range(1,11):
        print(i*j)
    print("\n")