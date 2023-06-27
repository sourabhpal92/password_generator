import random
import string

def generate_password(length=12):
    # Define the password criteria based on CIDM policy
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Create a pool of characters to choose from
    pool = lowercase_letters + uppercase_letters + numbers + special_characters

    # Ensure that the generated password meets CIDM policy requirements
    while True:
        password = ''.join(random.choice(pool) for _ in range(length))
        if (any(char in lowercase_letters for char in password)
                and any(char in uppercase_letters for char in password)
                and any(char in numbers for char in password)
                and any(char in special_characters for char in password)):
            break

    return password

# Usage example:
generated_password = generate_password()
print(generated_password)
