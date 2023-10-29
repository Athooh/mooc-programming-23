# Write your solution here
def row_correct(sudoku: list, row_no: int):
    dgts = list(range(1, 10))
    for dgt in sudoku[row_no]:
        if sudoku[row_no].count(dgt) > 1 and dgt in dgts:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    dgts = list(range(1, 10))
    for row in sudoku:
        dgt = row[column_no]
        if sum(1 for row in sudoku if row[column_no] == dgt) != 1 and dgt in dgts:
            return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    dgts = list(range(1, 10))
    block = [sudoku[i][j] for i in range(row_no, row_no + 3) for j in range(column_no, column_no + 3)]

    for dgt in block:
        if block.count(dgt) > 1 and dgt in dgts:
            return False

    return True

def sudoku_grid_correct(sudoku: list):
    for row_no in range(9):
        if not row_correct(sudoku, row_no):
            return False

    for column_no in range(9):
        if not column_correct(sudoku, column_no):
            return False

    for row_no in range(0, 9, 3):
        for column_no in range(0, 9, 3):
            if not block_correct(sudoku, row_no, column_no):
                return False

    return True

if __name__ == '__main__':

    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1],
    ]

    print(sudoku_grid_correct(sudoku1))  
    print(sudoku_grid_correct(sudoku2))  
