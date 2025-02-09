try:
    n = int(input("Enter n: "))
    if n<=0:
        raise Exception("n should be positive number!")
    s = []
    f = []
    A = []
    new = []
    for i in range(n):
        s.append(int(input(f"Start for {i+1}: ")))
        f.append(int(input(f"End for {i+1}: ")))
        if s[i]>f[i]:
            raise Exception("Start should not be bigger than finish.")
        A.append(i)
    for i in range(n):
        for j in range(i+1, n):
            if s[i]>s[j] or (s[i]==s[j] and f[i]>f[j]):
                s[i], s[j] = s[j], s[i]
                f[i], f[j] = f[j], f[i]
                A[i], A[j] = A[j], A[i]

    print("s =", s)
    print("f =", f)
    print("A =", A)
    j = 0
    new.append(A[j])
    for i in range(1,n):
        if s[i]>=f[j]:
            new.append(A[i])
            j = i
    print("new =", new)
except Exception as e:
    print(e)