''' Write a program that asks the user how many Fibonnaci
numbers to generate and then generates them.'''

n = int(input('Enter no of Fibonnaci terms - '))
n1, n2 = 0, 1
count = 0
if n <= 0:
 print('Invalid!! Enter a +ve no.')
elif n == 1:
 print('Fibonnaci sequence of', n, 'terms is')
 print(n1)
else:
 print('Fibonnaci sequence of', n, 'terms is')
 while count < n:
  print(n1)
  nth = n1 + n2
  n1 = n2
  n2 = nth
  count = count + 1