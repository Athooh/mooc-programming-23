# Write your solution here
def print_sudoku(sudoku: list):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if sudoku[i][j] == 0:
                print("_", end=" ") 
                
            else:
                print(str(sudoku[i][j]), end=" ")
        print()  



    
def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    if 1 <= number <= 9:
        sudoku[row_no - 1][column_no - 1] = number  
    else:
        print("Invalid number. Please enter a digit between 1 and 9.")

if  __name__ == "__main__":

    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


    print("Initial sudoku grid:")
    print_sudoku(sudoku)


    add_number(sudoku, 1, 1, 2) 
    add_number(sudoku, 2, 3, 7)
    add_number(sudoku, 6, 8, 3)

    print("\nThree numbers added:")
    print_sudoku(sudoku)
