import secrets
import string

def generate_password(length):
    letters = string.ascii_letters   # a-z, A-Z
    digits = string.digits           # 0-9
    symbols = string.punctuation     # special characters

    
    all_chars = letters + digits + symbols

    
    password = [
        secrets.choice(digits),
        secrets.choice(letters),
        secrets.choice(symbols)
    ]

    
    password += [secrets.choice(all_chars) for _ in range(length - 3)]


    
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

n=int(input("Password length:"))
print(generate_password(n))