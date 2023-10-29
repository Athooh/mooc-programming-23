# Write your solution here
import string

def separate_characters(my_string: str):
    ascii_letters = string.ascii_letters
    punctuation = string.punctuation
    lower_upper_char = ""
    punctuation_char =""
    other_char = ""

    for char in my_string:
        if char in ascii_letters:
            lower_upper_char += char
        elif char in punctuation:
            punctuation_char += char
        else:
            other_char += char

    return (lower_upper_char, punctuation_char, other_char)

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])


