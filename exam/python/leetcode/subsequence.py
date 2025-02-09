def isSubsequence(s: str, t: str) :
    i = 0
    j = 0
    while i<len(t):
        while i<len(t) and j<len(s):
            if s[j]==t[j]:
                j+=1
            i+=1
        return True
    return False

print(isSubsequence("abc", "ahbgdc"))