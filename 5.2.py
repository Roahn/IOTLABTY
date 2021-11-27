print("Enter file to open")
filepath = input()
file = open(filepath,"r");
count = 0;

for each in file:
    print(each, end= "")
    count =count +1

print(count)