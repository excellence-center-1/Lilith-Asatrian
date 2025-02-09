#from start to end

# try:
#     def fib(n):
#         if n<0:
#             raise Exception("n must not be negative")
#         if n==0:
#             return [0]
#         if n==1:
#             return [0,1]
#         fib = [0,1]
#         for i in range(2, n+1):
#             fib.append(fib[i-1]+fib[i-2])
#         return fib[n]
    
#     n = int(input("n="))
#     print(fib(n))

# except Exception as e:
#     print(e)

#recursive

# try:
#     def fib(n):
#         if n<=0:
#             raise Exception("n should not be negative")
#         if n==1:
#             return 0
#         if n==2:
#             return 1
#         return fib(n-1)+fib(n-2)

#     n = int(input("Enter n="))
#     print(fib(n))

# except Exception as e:
#     print(e)

try: 
    fib_memo = {}
    def fib(n):
        if n<=0:
            raise Exception("n must not be negative")
        if n in fib_memo: 
            return fib_memo[n]
        if n==1:
            value = 0
        elif n==2:
            value = 1
        else:
            value = fib(n-1)+fib(n-2)
        fib_memo[n] = value
        return value
        
    n = int(input("n="))
    print(fib(n))
except Exception as e:
    print(e)