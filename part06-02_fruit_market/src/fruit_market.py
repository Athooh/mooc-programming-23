# write your solution here
def read_fruits():
    fruit_dict = {}
    fruit_list = []
    
    with open("fruits.csv", "r") as frts:
        for line in frts:
            line = line.replace("\n", "")
            fruit_item = line.split(";")
            fruit_list.append(fruit_item)
        
        for item in fruit_list:
            fruit_dict[item[0]] = float(item[1])
            
    return fruit_dict
if __name__ == "__main__":
    print(read_fruits())
        
        