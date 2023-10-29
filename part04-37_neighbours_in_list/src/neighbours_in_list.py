# Write your solution here
def longest_series_of_neighbours(input_list):
    longest_length = 0
    current_length = 1

    for i in range(1, len(input_list)):
        if abs(input_list[i] - input_list[i - 1]) == 1:
            current_length += 1
        else:
            longest_length = max(longest_length, current_length)
            current_length = 1

    return max(longest_length, current_length)
if __name__ == '__main__':
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list)) 
