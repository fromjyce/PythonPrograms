A = [[1,2],[4,5]]
B = [[7,8],[9,10]]
rows = len(A)
cols = len(A[0])

E = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        E[i][j] = A[i][j] / B[i][j]
print("Division of matrices: \n", E)