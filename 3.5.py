# 5. Write a program that
# takes a list and returns a new list that contains all the elements of the first
# list minus all the duplicates.


l=[]
a=0
for i in range(1,6):
  a=int(input())
  l.append(a)

res = []
for i in l:
    if i not in res:
        res.append(i)
print(res)