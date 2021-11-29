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