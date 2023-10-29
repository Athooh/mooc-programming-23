# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    if function == 0:
        print("Bye now!")
        break
    elif function == 1:
        diary_entry = input("Diary entry: ")
        with open("diary.txt", "a") as df: 
            df.write(diary_entry + "\n")
            print("Diary saved")
    elif function == 2:
        print("Entries: ")
        with open("diary.txt", "r") as df:
            data = df.read()
            print(data)