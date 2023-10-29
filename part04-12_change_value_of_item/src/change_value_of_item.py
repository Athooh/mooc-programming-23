# Write your solution here
num_list = list(range(1, 5 + 1))

while True:
    idx = int(input("Index:"))
    if idx != -1:
        new_value = int(input("New value:"))
        num_list[idx] = new_value
        print(num_list)
    else:
        break
    
    
