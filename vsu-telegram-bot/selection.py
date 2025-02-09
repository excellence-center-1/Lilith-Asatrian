import random
A = [3,5,12,0,-5,6,2,13]

random.shuffle(A)
print(A)
min_1 = A[0]
min_2 = A[1]

for i in range(1, len(A)):
    if A[i]<min_1:
        c = min_1
        min_1 = A[i]
        min_2 = c
    elif A[i]<min_2:
            min_2 = A[i]

print("min_1: ", min_1)
print("min_2: ", min_2)

