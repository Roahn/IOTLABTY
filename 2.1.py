#Find the number from 1000 to 2000 which are divisible by 7 but not the multiple  of 5


for i in range(1000,2001,1):

    if((i%7==0) and (i%5!=0)):
        print(i)



