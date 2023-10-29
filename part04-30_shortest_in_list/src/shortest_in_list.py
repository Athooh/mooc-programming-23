# Write your solution here
def shortest(my_list):
    shrt_word = ""
    mn_wd = min(len(word) for word in my_list)
    for i in my_list:
        if len(i) == mn_wd:
            shrt_word = i  
            
    return shrt_word
if __name__ == '__main__':
    my_list = ['Alan', 'Susan', 'Seymour', 'Kim', 'Susan']
    result = shortest(my_list)
    print(result)
        