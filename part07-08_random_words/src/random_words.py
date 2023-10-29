import random

def words(n: int, beginning: str):
    with open('words.txt', 'r') as file:
        all_words = []
        for line in file:
            line = line.strip()
            all_words.append(line)

    filtered_words = [] 
    for word in all_words:
        if word.startswith(beginning):
            filtered_words.append(word)

    if len(filtered_words) < n:
        raise ValueError(f"Not enough words starting with '{beginning}' in the file.")

    selected_words = random.sample(filtered_words, n)

    return selected_words

if __name__ == "__main__":

    try:
        word_list = words(3, "ca")
        for word in word_list:
            print(word)
    except ValueError as error:
        print(error)

