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