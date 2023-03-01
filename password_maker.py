import random

#setting available characters for password generation
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?^_"

symbol_kit = ""

n = int(input("Enter the number of passwords to receive: "))
length = int(input("Enter the desired password length: "))
add_digit = input("Enable numbers? (y = yes, n = no) ").lower().strip()
add_lowercase = input("Include capital letters? (y = yes, n = no) ").lower().strip()
add_uppercase = input("Enable lowercase letters? (y=yes, n=no) ").lower().strip()
add_punctuation = input("Include characters like !#$%&*+-=?@^_? (y = yes, n = no) ").lower().strip()

#if symbols for a password were wished,
#then these characters are added to a variable
#that contains the characters to be used in generation

if add_digit.lower() == "y":
    symbol_kit += digits
if add_lowercase.lower() == "y":
    symbol_kit += lowercase_letters
if add_uppercase.lower() == "y":
    symbol_kit += uppercase_letters
if add_punctuation.lower() == "y":
    symbol_kit += punctuation

password = ""
while n != 0:
    for j in range(length):
        password += random.choice(symbol_kit) # every character in the password is randomised
    print(password)
    password = ""
    n -= 1
