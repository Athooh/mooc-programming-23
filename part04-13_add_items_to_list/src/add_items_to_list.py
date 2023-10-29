# Write your solution here
items = int(input("How many items:"))
item_list = []
for i in range(1, items + 1):
    itm = int(input(f"Item {i}: "))
    item_list.append(itm)
    
print(item_list)