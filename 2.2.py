# Take the number in a hex which are divisible by 5


#base 16
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
# 0 1 2 3 4 5 6 7 8 9 A  B   C  D  E  F 
print("Check the hexnumber is divisible by 5 or not")
print("Enter Number in hexadecimal")
num =int(input(),16)

#print(num)
if(num %5==0):
    print(num," is divisible by 5")
else:
    print(num,"is not divisible by 5")

