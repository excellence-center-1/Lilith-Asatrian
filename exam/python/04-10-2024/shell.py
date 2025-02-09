A = []
n = int(input("n="))
for i in range(n):
    A.append(int(input(f"Enter A[{i}] element: ")))
#4,5,6,7,-2,-1,0,-8
gap = n//2 #4

while gap!=0:
    for i in range(gap, n):
        key = A[i]
        j = i
        while j>0 and key<A[j-gap]:
            A[j] = A[j-gap]
            j-=gap
        A[j] = key
    gap //= 2

print(A)


