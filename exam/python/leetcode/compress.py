def compress(chars):
    s = ""
    i = 0
    n = len(chars)
    pointer = 0
    while i<n:
        count = 0
        a=chars[i]
        while i<n and chars[i]==a:
            count+=1
            i+=1
        chars[pointer]=a
        pointer+=1
        if count>1:
            for j in str(count):
                chars[pointer]=j
                pointer+=1
    
    return pointer

print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))