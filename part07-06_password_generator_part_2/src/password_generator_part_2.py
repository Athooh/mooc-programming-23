# Write your solution here
import random
import string

def generate_strong_password(length, include_numbers=True, include_special_chars=True):
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    special_chars = '!?=+-()#'
    characters = lowercase_letters
    
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += special_chars

    password_list = random.sample(lowercase_letters, 1)  
    if include_numbers:
        password_list.append(random.choice(string.digits))

    if include_special_chars:
        password_list.append(random.choice(special_chars))

    remaining_length = length - len(password_list)
    password_list.extend(random.sample(characters, remaining_length))

    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

if __name__ == '__main__':
    for i in range(10):
        print(generate_strong_password(8, True, True))
