#Nimas Dimitrios DimitrisNimas.gr
#Password Generator using Python

import string
import random
import requests
import hashlib

def generate(length):
    while True:
        password = ''.join(random.choice(string.ascii_uppercase) +
                           random.choice(string.ascii_lowercase) +
                           random.choice(string.digits) +
                           random.choice(string.punctuation))
                           
        password += ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(pass_length - 4))
        if not is_pwned(password):
            return password

def is_pwned(password):
    hash_prefix = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()[:5]
    response = requests.get(f'https://api.pwnedpasswords.com/range/{hash_prefix}')
    hashes = (line.split(':') for line in response.text.splitlines())
    return False

if __name__ == "__main__":
    while True:
        try:
            pass_length = int(input("Enter password length (8-32): "))
            if pass_length < 8 or pass_length > 32:
                print("Password length must be between 8 and 32.")
            else:
                generated = generate(pass_length)
                print("The Password is:", generated)
        except ValueError:
            print("Please enter a valid number.")
