'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    if row_check(sudoku):
        if column_check(sudoku):
            if sub_sudoku(sudoku):
                return True
    return False

def row_check(sudoku):
    '''
    Checking row condition
    '''
    for row in sudoku:
        if sudoku.count(set(row)) == 9:
        #and sum(row) == 45:
            return True
        return False

def column_check(sudoku):
    '''
    Checking column condition
    '''
    trans_pose = []
    for i in range(len(sudoku)):
        for row in sudoku:
            for colu in row[i]:
                row.append(colu)
            trans_pose.append(row)
    return row_check(trans_pose)

def sub_sudoku(sudoku):
    '''
    Checking for sub matrix of sudoku
    '''
    mat = []
    for row in sudoku:
        lst = row[0:3:1]
        mat.append(lst)
    for colu in sudoku:
        lst = colu[0:3:1]
        mat.append(lst)
    if sudoku.set(mat) == 9:
        return True
    return False

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
    # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
