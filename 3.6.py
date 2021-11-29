no = int(input())

count= 0
while(int(no>0)):
    digit=0
    digit = no %10 ;
    #print(digit)
    no = no//10
    count = count+1
print(count)