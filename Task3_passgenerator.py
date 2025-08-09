# Codesoft Python Internship Project 3 - Random Password Generator
# Created by Vaibhav Sharma

import random
import string

def generate_password(length):
    if length < 6:
        print("⚠ For better security, use a length of at least 6.")
        return ""

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all characters
    all_characters = lowercase + uppercase + digits + special_characters

    # Ensure password has at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length
    password += random.choices(all_characters, k=length - 4)

    # Shuffle for randomness
    random.shuffle(password)

    return ''.join(password)

print("🔐 Welcome to Random Password Generator!")

try:
    user_length = int(input("Enter desired password length: "))
    if user_length <= 0:
        print("❌ Please enter a positive number.")
    else:
        password = generate_password(user_length)
        if password:
            print(f"\n✅ Random Generated Password: {password}")
except ValueError:
    print("❌ Invalid input. Please enter a valid number.")
