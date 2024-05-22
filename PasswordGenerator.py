# for number in range(1, 11, 3):
#     print (number)
# total = 0
# for number in range (1, 101):
#     total += number
# print (total)


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# ----MY SOLUTION----

# string_letters = ""
# string_numbers = ""
# string_symbols = ""
# for count_letter in range(1, nr_letters+1) :
#     random_letter = random.randint(0,len(letters))
    
#     string_letters += letters[random_letter-1]

# for count_symbols in range(1, nr_symbols+1) :
#     random_symbols = random.randint(0,len(symbols))
#     string_symbols += symbols[random_symbols-1]
    
    
# for count_numbers in range(1, nr_numbers+1) :
#     random_numbers = random.randint(0,len(numbers))
    
#     string_numbers += numbers[random_numbers-1]


# print(combined_string = string_letters+string_symbols+string_numbers)

#---UDEMY SOLUTION---

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
