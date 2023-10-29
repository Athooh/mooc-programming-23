# Write your solution here
def invert(dictionary: dict):
    invert_dict = {}
    for k, v in dictionary.items():
        invert_dict[v] = k
    
    dictionary.clear()
    dictionary.update(invert_dict)

if __name__ == '__main__':
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
    