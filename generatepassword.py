import random
import string

def generate_password(length, use_uppercase, use_digits, use_symbols):
    """Generate a random password of given length with specified character types"""
    # define characters to use for password based on specified requirements
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # generate password using random.choices()
    password = ''.join(random.choices(characters, k=length))

    return password

# get password requirements from user
password_length = int(input("Enter desired password length: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
use_digits = input("Include digits? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"

# generate password based on user requirements
password = generate_password(password_length, use_uppercase, use_digits, use_symbols)
print(password)
