import random
import string

# Prompt the user for password length and complexity
length = int(input("Enter desired password length: "))
uppercase = input("Include uppercase letters? (y/n): ")
lowercase = input("Include lowercase letters? (y/n): ")
numbers = input("Include numbers? (y/n): ")
symbols = input("Include symbols? (y/n): ")

# Define character sets based on user input
chars = ""
if uppercase == "y":
    chars += string.ascii_uppercase
if lowercase == "y":
    chars += string.ascii_lowercase
if numbers == "y":
    chars += string.digits
if symbols == "y":
    chars += string.punctuation

# Generate a random password using the specified character set
password = ''.join(random.choice(chars) for i in range(length))

# Print the generated password
print("Your randomly generated password is:", password)
