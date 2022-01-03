# 4. Print the pattern
# : 


# 5 4 3 2 1


# 4 3 2 1


# 3 2 1


# 2 1


# 1


no = int(input())
for i in range(1,no+1):
    for j in range(no-i+1,0,-1):
        print(j,end=" ")

    print("\n")

