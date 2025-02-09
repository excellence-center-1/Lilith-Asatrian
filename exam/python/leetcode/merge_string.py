def mergeAlternately(word1: str, word2: str):
    i = 0
    j = 0
    a = ""
    while i<len(word1) and j<len(word2):
        k = 0
        if k%2==0 and k!=1:
            a+=word1[i]
            i+=1
        else:
            a+=word2[j]
            j+=1
        k+=1
    if i<len(word1):
        a+=word1[i:]
    if j<len(word2):
        a+=word2[j:]
    return a

print(mergeAlternately("abc", "pqr"))