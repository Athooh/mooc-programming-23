# Write your solution here
def find_words(search_term: str):
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()

    matching_words = []

    if search_term.startswith('*'):
        suffix = search_term[1:]
        matching_words = [word for word in words if word.endswith(suffix)]

    elif search_term.endswith('*'):
        prefix = search_term[:-1]
        matching_words = [word for word in words if word.startswith(prefix)]
    
    else:
        matching_words = [word for word in words if word == search_term]


    if '.' in search_term:
        wildcard_pattern = search_term.replace('.', '')
        
        import re
        matching_words = [word for word in words if re.match(wildcard_pattern, word)]

    return matching_words

if __name__ == '__main__':
    print(find_words("*vokes"))