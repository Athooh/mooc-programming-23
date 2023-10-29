# Write your solution here
def no_shouting(my_list):
    not_upper = []
    for word in my_list:
        if word.isupper():
            continue
        else:
            not_upper.append(word)
    
    return not_upper
if __name__ == '__main__':
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
