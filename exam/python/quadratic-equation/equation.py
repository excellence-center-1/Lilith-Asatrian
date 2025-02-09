import math
def equation(a,b,c):
    try:
        if a==0:
            return -c/b 
        else:
            D = b**2-4*a*c
            if D<0:
                raise Exception("Discriminant can't be negative.")
            elif D==0:
                return -b/(2*a)
            else:
                x1 = (-b+math.sqrt(D))/(2*a)
                x2 = (-b-math.sqrt(D))/(2*a)
                return x1, x2
    except Exception as e:
        print(e)
