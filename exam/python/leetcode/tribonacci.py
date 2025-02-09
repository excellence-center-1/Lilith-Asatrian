dict = {
    0: 0,
    1: 1,
    2: 1
}
def tribonacci(n):
    if n==0:
        return dict[0]
    elif n==1:
        return dict[1]
    elif n==2:
        return dict[2] 
    else:
        if n not in dict.keys():
            elem = tribonacci(n-3)+tribonacci(n-2)+tribonacci(n-1)
            dict[n] = elem
        else:
            return dict[n]

print(tribonacci(4))