#Find Prime number from 1 to 100

i=1
no =1
count =0


print("Prime Numbers from 1 to 100  are : \n\n\n\t")
for i in range (1,101,1):
    
    count =0
    for j in range (1,101,1):
        if(i%j ==0):
            count = count +1
    if(count<3):
        print(i)
        