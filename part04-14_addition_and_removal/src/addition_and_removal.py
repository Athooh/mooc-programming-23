# Write your solution here
numbers = []
num = 0
print("The list is now []")
while True:
    cmd = input("a(d)d, (r)emove, e(x)it: ")
    if cmd == "d":
        num += 1
        numbers.append(num)
        print(f"The list is now {numbers}")
    elif cmd == "r":
        numbers.pop()
        num -= 1
        print(f"The list is now {numbers}")
    else:
        print("Bye!")
        break
        
        
        