def min(a, *params):
    min = abs(params[0]-a)
    val = params[0]
    for i in params:
        diff = abs(i-a)
        if diff<min:
            min = diff
            val = i
    return val

print(min(-2, -2))
print(min(5,3,1921,1,4))

