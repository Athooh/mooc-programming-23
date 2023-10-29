# Write your solution here
def distinct_numbers(my_list):
    my_list = list(set(my_list))
    return sorted(my_list)

if __name__ == '__main__':
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))