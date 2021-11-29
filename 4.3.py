'''generate a python list of all even numbers between 4 to 40'''

even_no = []
for i in range(4, 41):
 if i % 2 == 0:
     even_no.append(i)

print(even_no)