# Write your solution here
def length_of_longest(my_list):
    lngst_word = 0
    for i in my_list:
        if len(i) < lngst_word:
            continue
        else:
            lngst_word = len(i)
    
    return lngst_word

if __name__ == '__main__':
    my_list = ['Alan', 'Grace', 'Frances', 'Kim', 'Susan']
    result = length_of_longest(my_list)
    print(result)