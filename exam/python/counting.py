A = [2,5,0,3,2,3,0,3]

n = 8
R = [0]*(n)
m = max(A)
C = [0]*(m+1)

for i in range(m+1):
    count = 0
    for j in range(n):
        if A[j] == i:
            count += 1
    C[i] = count
    
for i in range(1, m+1):
    C[i] += C[i-1]

print(C)

for i in range(n-1, -1, -1):
    ind = A[i]
    C[ind] -= 1
    r_ind  = C[ind]
    R[r_ind] = A[i]

print("resulting array: ", R)