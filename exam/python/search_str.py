def match_str(s, k):
    j = 0
    i = 0
    n = len(s)
    m = len(k)
    L = []
    q = 0
    while i<n:
        while i<n and j<m:
            if s[i]==k[j]:
                j+=1
            else:
                j = 0
            i+=1
        if j==m:
            q+=1
            L.append(i-m)
            j = 0
    return q, L

print(match_str("ananan", "an"))


        

