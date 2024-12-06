"""
Topics Covered:
1. For loops
2. Sum and Max over a list
3. For loops with range() function

Project Description:
1. Generate a password for a user with their desired number of letters, symbols, and numbers
2. Easy level: generate the password in sequence. For example, if the user wants 4 letters, 2 symbols, and 3 numbers then the password might look like this: fgDx$*924
3. Hard level: randomize the order of the characters in the password. For example, the above password might look like this: 2*Df9$gx4

Completed: 12/6/2024
"""
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy level: Generate the password in sequence
pw_letters = ''
for letter in range(0, nr_letters):
    pw_letters += random.choice(letters)

pw_symbols = ''
for symbol in range(0, nr_symbols):
    pw_symbols += random.choice(symbols)

pw_numbers = ''
for number in range(0, nr_symbols):
    pw_numbers += random.choice(numbers)

print(f"Your password is: {pw_letters + pw_symbols + pw_numbers}")

# Hard level: Generate the password with each character in a random order
pw_list = []
for letter in range(0, nr_letters):
    pw_list.append(random.choice(letters))

for symbol in range(0, nr_symbols):
    pw_list.append(random.choice(symbols))

for number in range(0, nr_numbers):
    pw_list.append(random.choice(numbers))

print(pw_list)
random.shuffle(pw_list)
print(pw_list)

random_pw = ''
for item in pw_list:
    random_pw += item

print(f"Your password is: {random_pw}")
