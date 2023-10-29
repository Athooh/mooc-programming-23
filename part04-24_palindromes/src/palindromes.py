# Write your solution here
def palindrome(word):
    if word[0:] == word[:-1]:
        return True
    else:
        return False

def main(word):
    while True:
        word = input("Please type in a palindrome: ")
        if word[0:] == word[:-1]:
            print(f"{word} is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")
            word = input("Please type in a palindrome: ")
if __name__ == "__main__":
    print(palindrome(word))
    main(word)


# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
