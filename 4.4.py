'''Write a recursive function to calculate the sum of numbers
from 0 to 50'''
def summation(x):
   if x <= 1:
    return x
   return x + summation(x - 1)


x = 50
print(summation(x))
