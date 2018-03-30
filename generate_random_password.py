import random

def generate_password(cant):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!#$%&()*+-.<=>?[]^_{|}~'
    password = ''
    for c in range(cant):
        password += random.choice(chars)
    return password

print(generate_password(40))
#Output: OU3i=%r=~jQL|aKQmyqAdV9fY9gH8f(XRkqrU_Ce