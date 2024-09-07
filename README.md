# Password Generator
Welcome to the Password Generator repository! This project provides a simple yet powerful password generator tool that you can use to create secure passwords based on your preferences.

## Features

- **Customizable Length**: Specify the desired length of your password.
- **Uppercase Letters**: Option to include uppercase letters.
- **Digits**: Option to include numbers.
- **Symbols**: Option to include special characters.

## Usage

To generate a password, use the `generate_password` function with the following parameters:

- `length` (int): Desired length of the password.
- `use_uppercase` (bool): Whether to include uppercase letters.
- `use_digits` (bool): Whether to include digits.
- `use_symbols` (bool): Whether to include symbols.

### How It Works
The generate_password function determines which characters to include in the password based on user-specified requirements and generates the password using the random.choices() function to randomly select characters from the string.

### Installation
You can clone the repository using the following command:
```github
git clone https://github.com/hemilynara/GeneratePassword.git
```
