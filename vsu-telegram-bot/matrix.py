# def is_prime(k):
#     """
#     Checks if the k number is prime
#     """
#     if k==1:
#         return False
#     flag = True
#     i = 2
#     while i<=k//2 and flag:
#         if k%i==0:
#             flag = False
#         i+=1

#     return flag

# def fl_prime(k, q):
#     """
#     Generates a list of prime numbers starting from k+1 with a specified quantity.
#     """
#     arr = []
#     i = 0
#     j = k+1
#     while i<q:
#         if is_prime(j):
#             arr.append(j)
#             i+=1
#         j+=1
#     return arr

# try:
#     n = int(input("Enter the size of matrix: "))
#     if n<=0:
#         raise Exception("n should be natural")
#     k = int(input("Enter k: "))
#     if k<=0:
#         raise Exception("k should be natural")
    
#     #Prime numbers list creation
#     count = n*n-n+1
#     l_prime = fl_prime(k, count)
#     print(f"List of prime numbers after {k}:", l_prime)

#     d_el_ind  = len(l_prime)//2
#     d_el = l_prime[d_el_ind]
#     l_prime.pop(d_el_ind)
#     A = []
#     c = 0
#     new_c = d_el_ind

#     for i in range(n):
#         A.append([])
#         for j in range(n-i-1):
#             A[i].append(l_prime[c])         
#             c+=1
#         A[i].append(d_el)
#         for j in range(n-i, n):
#             A[i].append(l_prime[new_c])
#             new_c+=1
#     print("-------------")
#     # A = [[str(A[i][j]) for j in range(n)] for i in range(n)]
#     # for x in A:
#     #     print(' '.join(x))

#     for row in A:
#         print(' '.join([str(elem) for elem in row]))
# except ValueError as e:
#     print("Conversion failed: ", e)
# except Exception as e:
#     print(e)

print("Press y to exit")

while True:
    data = input("Enter to exchange: ")

    if data.lower() == 'y':
        break
    money = int(data)
    if money<0:
        print("Amount must be positive")
        continue

    cache = round(money/480,2)
    print("To issue: ", cache, "$")

print("The work of exchange has been completed!")