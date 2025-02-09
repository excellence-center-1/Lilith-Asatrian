n = int(input("n="))
k = int(input("k="))

A = [[0]*(k+1) for _ in range(n+1)]

A[0][0] = 1

for j in range(1, k+1):
    for i in range(j, n+1):
        A[i][j] = (i-1)*A[i-1][j] + A[i-1][j-1]

print(A[n][k])