# Write your solution here
def all_the_longest(my_list):
    long_list = []
    max_wd = max(len(word) for word in my_list)
    for i in my_list:
        if len(i) == max_wd:
            long_list.append(i)
    
    return long_list
if __name__ == '__main__':
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) 