num_matrices = int(input("Enter the number of matrices you want to input: "))
sum_matrix = None
dimensions_match = True  # flag variable
for m in range(num_matrices):
    row = int(input("Enter the number of rows for matrix {}: ".format(m+1)))
    col = int(input("Enter the number of columns for matrix {}: ".format(m+1)))
    matrix = []
    for i in range(row):
        row_list = []
        for j in range(col):
            element = int(input("Enter the element at position ({},{}): ".format(i+1, j+1)))
            row_list.append(element)
        matrix.append(row_list)

    if sum_matrix is None:
        sum_matrix = [[0 for j in range(col)] for i in range(row)]

    if len(matrix) != len(sum_matrix) or len(matrix[0]) != len(sum_matrix[0]):
        dimensions_match = False  # set flag to False
        print("Error: Dimensions of matrices do not match. Aborting...")
        break

    for i in range(row):
        for j in range(col):
            sum_matrix[i][j] += matrix[i][j]

    print("Matrix {}:".format(m+1))
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end=" ")
        print()

if dimensions_match and sum_matrix is not None:  # check flag and print sum matrix
    print("Sum Matrix:")
    for i in range(len(sum_matrix)):
        for j in range(len(sum_matrix[0])):
            print(sum_matrix[i][j], end=" ")
        print()
