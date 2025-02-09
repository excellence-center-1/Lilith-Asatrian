def remove_stars(s):
    stack = []
    for i in s:
        if i!='*':
            stack.append(i)
        else:
            stack.pop()
    s = ''.join(stack)
    return s

print(remove_stars("leet**cod*e"))