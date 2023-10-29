# Write your solution here
def row_sums(my_matrix: list):
    
    for nested_list in my_matrix:
        nested_list.append(sum(nested_list))
    
    # sum_list = [sum(row) for row in my_matrix]
        
    # for i in range(len(my_matrix)):
    #     my_matrix[i].append(sum_list[i])
        
if __name__ == '__main__':
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)
