# write your solution here
def matrix_sum():
    num_list = []
    with open("matrix.txt") as f:
        for line in f:
            line = line.replace("\n", "")
            row = line.split(",")
            for num in row:
                num_list.append(int(num))
    
    return sum(num_list)
    
def matrix_max():
    num_list = []
    with open("matrix.txt") as f:
        for line in f:
            line = line.strip()
            line = line.replace("\n", "")
            ech_list = line.split(",")
            num_list.extend(ech_list)
            
    nw_list = [int(x) for x in num_list]
    largest = max(x for x in nw_list)
    return largest
    
def row_sums():
    sum_row = []
    ech_row = []
    with open("matrix.txt") as f:
        for line in f:
            line = line.strip()
            ech_row = line.split("\n")
            for row in ech_row:
                n = row.split(",")
                nw_row = [sum(int(x) for x in n)]
                sum_row.extend(nw_row)
    
    return sum_row

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())