# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    new_string = "".join([char for char in string if char not in forbidden])
    return new_string

if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)