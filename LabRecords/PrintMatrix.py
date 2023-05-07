#PrintMatrix
num_matrices = int(input("Enter the number of matrices you want to input: "))
for m in range(num_matrices):
    # Ask user to input the row and column value
    row = int(input("Enter the number of rows for matrix {}: ".format(m+1)))
    col = int(input("Enter the number of columns for matrix {}: ".format(m+1)))

    # Initialize an empty matrix
    matrix = []

    # Ask user to input the elements of the matrix
    for i in range(row):
        row_list = []
        for j in range(col):
            element = int(input("Enter the element at position ({},{}): ".format(i+1, j+1)))
            row_list.append(element)
        matrix.append(row_list)
    
    print("Matrix {}:".format(m+1))
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end=" ")
        print()