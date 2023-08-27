import secrets
import string
import pytest
from unittest.mock import patch

def generate_password(min_longitud=12):
    """
    Generates a password with a minimum length to ensure a certain level of security.
    
    Args:
        min_longitud (int): The minimum length of the password. Default is 12.
        
    Returns:
        str: The generated password.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    longitud = max(min_longitud, 12)
    while True:
        password = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        if any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password):
            return password

def main():
    """
    Prompt the user to enter the desired length for the password,
    generate a password with the desired length, and return the generated password.
    """
    MIN_LENGTH = 6
    while True:
        try:
            desired_length = int(input("Enter the desired length for the password: "))
            if desired_length <= MIN_LENGTH:
                print(f"The desired length must be greater than or equal to {MIN_LENGTH}.")
            else:
                break
        except ValueError as e:
            raise ValueError("Please enter a valid integer.") from e

    generated_password = generate_password(desired_length)

    return generated_password

if __name__ == '__main__':
    print(main())