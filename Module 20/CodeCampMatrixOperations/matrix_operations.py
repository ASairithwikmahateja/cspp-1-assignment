def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    pass

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    pass

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    dimensions = input()
    #print(dimensions)
    rows = int(dimensions.split(",")[0])
    #print(rows)
    columns = int(dimensions.split(",")[1])
    #print(columns)
    lst = []
    for i in range(rows):
        for j in range(columns):
            lst[i][j] = input().split(" ")
    return lst

def main():
    # read matrix 1
    m1 = read_matrix()
    # read matrix 2
    m2 = read_matrix()
    # add matrix 1 and matrix 2
    add_matrix(m1, m2)
    # multiply matrix 1 and matrix 2
    mult_matrix(m1, m2)

if __name__ == '__main__':
    main()
