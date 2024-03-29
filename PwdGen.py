import random
import string

def generate_password(len):
    ch = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(ch) for i in range(len))
    return password

# Get the desired length of the password from the user
input_length = int(input("Enter the length of the password: "))

# Generate and print the password
print("Generated Password:", generate_password(input_length))
