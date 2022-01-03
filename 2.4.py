import random

import array

max_len = 10

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

L_case_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

U_case_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '{', '}', '[', ']', ';', ':', ',', '<', '>', '/', '?']

conbined_list = digits + L_case_char + U_case_char + symbols

rand_digit = random.choice(digits)

rand_upper_c = random.choice(U_case_char)

rand_lower_c = random.choice(L_case_char)

rand_symbol = random.choice(symbols)

temp_password = rand_digit + rand_upper_c + rand_lower_c + rand_symbol

for i in range(max_len - 4):

    temp_password = temp_password + random.choice(conbined_list)

   

    temp_pass_list = array.array('u', temp_password)

    random.shuffle(temp_pass_list)

password = ""

for i in temp_pass_list:

    password = password + i

print(password)