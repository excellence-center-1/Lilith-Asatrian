try:
    # n = int(input("Input natural n: "))
    # if n<=0:
    #     raise Exception("n must be natural!")
    # A = []
    # for i in range(n):
    #     row = input(f"Input {i+1} row seperated by spaces: ").split()
    #     if len(row)!=n:
    #         raise Exception(f"Row {i+1} should contain {n} elements!")    
    #     A.append([int(x) for x in row])
    n = 3
    A = [
            [5,18,9],
            [-9,6,3],
            [12,4,-8]
        ]
    min_el = min(A[0])
    min_ind = 0
    max_el = max(A[0])
    max_ind = 0
    for i in range(n):
        if min(A[i])<min_el:
            min_el = min(A[i])
            min_ind = A[i].index(min_el)

    for i in range(n):
        if max(A[i])>max_el:
            max_el = max(A[i])
            max_ind = i

    B = []
    row = []
    #minimal element contating column
    for i in range(n):
        row.append(A[i][min_ind])
    B.append(row)
    #maximal element containing row
    B.append(A[max_ind])

    #first negative element containing column(if it exists)
    i = 0
    row = []
    flag = False
    while i<n and not flag:
        j = 0
        while j<n and not flag:
            if A[i][j]<0:
                flag = True
                for k in range(n):
                    row.append(A[k][j])
            else:
                j+=1
        i+=1
    if row:
        B.append(row)
    
    #first positive element containing row(if it exists)
    i = 0
    flag = False
    while i<n and not flag:
        j = 0
        while j<n and not flag:
            if A[i][j]>0:
                flag = True
                B.append(A[i])
            else:
                j+=1
        i+=1
    
    B = [[(str(B[i][j])) for j in range(len(B[i]))] for i in range(len(B))]
    for i in range(len(B)):
        print(' '.join(B[i]))
except ValueError as e:
    print("Conversion failed: ", e)
except Exception as e:
    print(e)