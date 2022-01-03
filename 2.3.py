#take 2-3 sentences and print them in front of each other .Calculate all the words in each senrtence and
#letters in individual words and capitalize each word in each sentence

inp_string_1 = input() 
inp_string_2 = input()
inp_string_3 = input()
inp_string_4 = input()


string = inp_string_1 + inp_string_2 + inp_string_3 + inp_string_4
print('The entered string after concatenation is - ', string)

a = len(string.split())
print('No. of words in the given string are - ', str(a))
print('Total no. of letters are - ', len(string))

print(string.title())
print()

print(string.upper())
print()

print(string.lower())
print()

String = string.split()
print(String)
[len(i) for i in String]