def gcdOfStrings(str1: str, str2: str):
    i = 1
    a = ""
    while i<len(str1) and i<len(str2):
        if len(str1)%i==0 and len(str2)%i==0:
            if str1[:i]==str2[:i]:
                a = str1[:i]
        i+=1
    return a

print(gcdOfStrings("ABABAB", "ABAB"))