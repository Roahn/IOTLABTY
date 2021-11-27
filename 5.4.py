#Number of word in the file
print("Enter file to open")
filepath = input()
file = open(filepath)
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))