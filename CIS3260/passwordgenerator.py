# passwordgenerator.py
import random
import string
from datetime import datetime, timedelta

# Function to generate a password
def generatepassword(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    """
    Generate a random password based on the given specifications.

    - length: Length of the password.
    - use_letters: Include letters in the password.
    - use_numbers: Include numbers in the password.
    - use_symbols: Include symbols in the password.

    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    character_pool = ''
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    return ''.join(random.choice(character_pool) for _ in range(length))

# Function to generate an expiration date for the password
def addexpiration(days_valid=30):
    
    #Generate an expiration date for the password.

    return datetime.now() + timedelta(days=days_valid)

# Function to analyze password strength
def analyze_password_strength(password):
    
    #Analyze the strength of a given password based on length and character variety.


    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digits = any(c.isdigit() for c in password)
    has_symbols = any(c in string.punctuation for c in password)

    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if has_lower and has_upper:
        score += 1
    if has_digits:
        score += 1
    if has_symbols:
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

# Function to generate multiple passwords
def generate_multiple_passwords(count=1, length=12, use_letters=True, use_numbers=True, use_symbols=True):
    """
    Generate multiple passwords with specified preferences.

    - count (int): Number of passwords to generate.
    - length: Length of each password.
    - use_letters: Include letters in the password.
    - use_numbers: Include numbers in the password.
    - use_symbols: Include symbols in the password.

    """
    passwords = []
    for _ in range(count):
        password = generatepassword(length, use_letters, use_numbers, use_symbols)
        strength = analyze_password_strength(password)
        passwords.append({"password": password, "strength": strength})
    return passwords