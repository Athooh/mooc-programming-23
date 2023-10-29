# Write your solution here
word_list = []
count = 0
word = input("Word: ")
while word not in word_list:
    word_list.append(word)
    count += 1
    word = input("Word: ")
else:
    print(f"You typed in {count} different words")
        
        