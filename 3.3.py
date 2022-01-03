# 3. Take a list from the
# user. Display the numbers which are divisible by 5 and if number >120. Stop
# the loop iteration.


l=[]
a=0
for i in range(1,11):
  a=int(input())
  l.append(a)
print("Output is :")
for i in l:
  if(i%5==0):
    if(i>120):
      break
    print(i)