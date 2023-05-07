def matrix_subtraction(matrix1, matrix2):
    # Check if dimensions of both matrices are the same
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Error: Dimensions of both matrices are not the same!")
        return None

    # Create a new matrix to store the result of the subtraction
    result_matrix = [[0 for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

    # Subtract corresponding elements of matrix1 and matrix2 and store the result in the result matrix
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result_matrix[i][j] = matrix1[i][j] - matrix2[i][j]

    # Return the result matrix
    return result_matrix

# Example usage
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result_matrix = matrix_subtraction(matrix1, matrix2)
print(result_matrix)
