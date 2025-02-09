x = int(input("x="))
n = int(input("n="))
s = 0

fact_a = 1
for i in range(1, n+1):
    a = 2*i
    for j in range(a-1, a+1):
        fact_a*=j

    b = i**2
    if b==1:
        fact_b = 1
    else:
        fact_b = fact_a
        for j in range(a+1, b+1):
            fact_b*=j
    s+=(fact_a+x)/fact_b

print("s=", round(s, 2))