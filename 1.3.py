#design a calculator having ball basic mathematical properties

no1=0
no2=0
while(1):

    print("Enter Number")
    no1 = int(input())
    print("Enter opeartion")
    str = input()
    print("Enter Number")
    no2 = int(input())
    print("-----------------------------")

    if(str =="+"):
        no2 = no1+no2
        print(no2)
    if(str =="-"):
        no2 = no1-no2
        print(no2)
    if(str =="*"):
        no2 = no1*no2
        print(no2)
    if(str =="/"):
        no2 = no1/no2
        print(no2)
            