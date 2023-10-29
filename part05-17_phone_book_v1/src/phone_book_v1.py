# Write your solution here
phone_book = {}

while True:
    command = int(input("command(1 search, 2 add, 3 quit): "))
    if command == 1:
        search_name = input("name: ")
        if search_name in phone_book.keys():
            print(phone_book[search_name])
        else:
            print("no number")
        
    elif command == 2:
        add_name = input("name: ")
        add_number = input("number: ")
        phone_book[add_name] = add_number
        print("ok!")
        
    else:
        print("quitting...")
        break