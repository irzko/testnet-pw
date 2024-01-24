import random
import secrets
import string


def random_username():
    name = random.choice(string.ascii_lowercase)
    name += ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(10, 16)))
    return name
     

def random_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password
