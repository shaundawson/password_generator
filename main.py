import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#store empty pw string
password = ""

# loop through all of the characters, generate a range based on user input
for char in range(1, nr_letters + 1):
  #generate random letter for each position
  random_char = random.choice(letters)
  # add random character to pw
  password += random_char

for char in range(1, nr_symbols + 1):
  random_sym = random.choice(symbols)
  password += random_sym

for char in range(1, nr_numbers + 1):
  random_num = random.choice(numbers)
  password += random_num
print(password)

print(f"Here is your new password: {password}")