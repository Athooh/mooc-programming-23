# Write your solution here
def first_word(sentence):
    sent1_list = sentence.split(' ')
    if len(sent1_list) >= 2:
        return sent1_list[0]

def second_word(sentence):
    sent2_list = sentence.split(' ')
    if len(sent2_list) >= 2:
        return sent2_list[1]

def last_word(sentence):
    sent3_list = sentence.split(' ')
    if len(sent3_list) >= 2:
        return sent3_list[-1]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))