# Write your solution here
original = []
ordered = []
while True:
    num = int(input("New item: "))
    if num != 0:
        original.append(num)
        ordered = sorted(original)
        print(f"The list now: {original}")
        print(f"The list in order: {ordered}")
    else:
        print("Bye!")
        break