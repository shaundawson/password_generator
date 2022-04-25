import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
nr_letters = input("How many letters would you like in your password?\n")
nr_symbols = input("How many symbols would you like?\n")
nr_numbers = input("How many numbers would you like?\n")
new_password = ""

#Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#Iterate through letters and choose number of characters based on nr_letters
for l in range(0,len(letters)):
  letters = random.sample(letters,int(nr_letters))
pw_letters = "".join(letters)
#Iterate through symbols and choose number of symbols based on nr_symbols
for s in range(0,len(symbols)):
  symbols = random.sample(symbols,int(nr_symbols))
pw_symbols = "".join(symbols)
#Iterate through numbers and choose number of numbers based on nr_numbers
for n in range(0,len(numbers)):
  numbers = random.sample(numbers,int(nr_numbers))
pw_numbers = "".join(numbers)

print(f"Here is your new password: {pw_letters}{pw_symbols}{pw_numbers} ")



#Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
