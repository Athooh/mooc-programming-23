# write your solution here
sentence = input("Write text: ")
wordlist = []

with open("wordlist.txt") as word:
    for line in word:
        line = line.replace("\n", "").strip()
        wordlist.append(line)
        
split_sentence = sentence.split(" ")
for wrd in split_sentence:
    if wrd.lower() not in wordlist:
        indx = split_sentence.index(wrd)
        split_sentence[indx] = "*" + wrd + "*" 

spell_checker = " ".join(split_sentence)
print(spell_checker)