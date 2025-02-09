try:
    n = int(input("Input the quantity of rows and columns: "))
    if n<=0:
        raise Exception("The quantity of rows and columns must be natural!")

    A = []
    
    for i in range(n):
        row = input(f"Input {i+1} row seperated by spaces: ").split()
        if len(row)!=n:
            raise Exception(f"Row {i+1} should contain {n} elements!")    
        A.append([int(x) for x in row])

    for i in range(n):
        print(A[i])
    
    print("--------------")
    
    d = A[0][0]
    for i in range(n):
        max_elem = max(A[i])
        min_elem = min(A[i])
        if A[i][i] == max_elem or A[i][i] == min_elem:
            continue
        d = A[i][i]
        A[i][i] = max_elem + min_elem
        ind_max = A[i].index(max_elem)
        ind_min = A[i].index(min_elem)
        A[i][ind_max] = int(d/2)
        A[i][ind_min] = max_elem
    
    A = [[str(A[i][j]) for j in range(n)] for i in range(n)]
    for i in range(n):
        print(' '.join(A[i]))
except ValueError as e:
    print("Conversion failed: ", e)
except Exception as e:
    print(e)
