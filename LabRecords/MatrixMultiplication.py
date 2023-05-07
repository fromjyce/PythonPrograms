A = [[1,2],[4,5]]
B = [[7,8],[9,10]]
rows = len(A)
cols = len(A[0])

F = [[0 for i in range(len(B[0]))] for j in range(len(A))]
for i in range(len(A)):
	for j in range (len(B[0])):
		for k in range (len(B)):
			F[i][j] = F[i][j] + (A[i][k]*B[k][j])
print("Multiplication of matrices: \n", F)