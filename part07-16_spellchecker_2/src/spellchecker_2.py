# Write your solution here
import difflib

def get_spell_check_feedback(text, word_list):
    def spell_check(word, word_list):
        closest_matches = difflib.get_close_matches(word, word_list)
        return closest_matches[0] if closest_matches else None

    def process_word(word, word_list):
        suggestion = spell_check(word, word_list)
        if suggestion:
            return f'*{word}* ({", ".join(suggestion)})'
        return word

    words = text.split()
    processed_words = [process_word(word.strip('.,?!()[]{}";:'), word_list) for word in words]
    return ' '.join(processed_words)


    word_list = []
    with open("wordlist.txt") as wrd_ist:
        # line = wrd_ist.readline()
        for line in wrd_ist:
            line = line.replace("\n", "").strip()
            word_list.append(line)
    
if __name__ == "__main__":
    while True:
        user_input = input("write text: ")
        if not user_input:
            break

        spell_checked_text = get_spell_check_feedback(user_input, word_list)
        print(spell_checked_text)
