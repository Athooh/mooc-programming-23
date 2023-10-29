# write your solution here
def largest():
    num_list = []
        
    with open("numbers.txt", "r") as fobj:
        for line in fobj:
            line = line.replace("\n", "")
            num_list.append(int(line))
    
    larg = max(x for x in num_list)
    return larg
if __name__ == "__main__":
    print(largest())
            
        

