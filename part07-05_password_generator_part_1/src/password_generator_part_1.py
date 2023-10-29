# Write your solution here
from random import sample

def generate_password(word_length):
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    sample_pass = sample(lowercase_letters, word_length)
    password = "".join(sample_pass)

    return password

if __name__ == '__main__':
    pass_list = []
    for i in range(10):
        password = generate_password(8)
        pass_list.append(password)
        print(password)
