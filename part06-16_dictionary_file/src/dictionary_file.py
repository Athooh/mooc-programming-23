# Write your solution here
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function_choice = input("Function: ")

    if function_choice == '1':
        finnish_word = input("The word in Finnish: ")
        english_word = input("The word in English: ")
        with open('dictionary.txt', 'a') as file:
            file.write(f"{finnish_word} - {english_word}\n")
        print("Dictionary entry added")
        
    elif function_choice == '2':
        found_entries = []
        search_term = input("Search term: ")
        with open('dictionary.txt', 'r') as file:
            for line in file:
                if search_term in line:
                    found_entries.append(line.strip())
        print(found_entries)
        for entry in found_entries:
            print(entry)

    elif function_choice == '3':
        print("Bye!")
        break

    else:
        print("Invalid input. Please try again.")

