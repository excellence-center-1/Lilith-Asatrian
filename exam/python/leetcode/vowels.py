def reverseVowels(s: str):
    list_v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    start = 0
    end = len(s)-1
    s = list(s)
    while start <= end:
        if s[start] in list_v and s[end] in list_v:
            s[start], s[end] = s[end], s[start]
            start+=1
            end-=1
        while s[start] not in list_v:
            start+=1
        while s[end] not in list_v:
            end-=1
        
    return "".join(s)

print(reverseVowels("leetcode"))