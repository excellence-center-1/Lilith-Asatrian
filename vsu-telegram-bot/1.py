# import math

# x = int(input("x="))
# p = 1
# n = int(input("n="))

# for i in range(1,n+1):
#     p*=(x+math.cos(i*x))/(2**i*math.factorial(i))

# print(p)

#կենտ ինդեքս ունեցող տարրերից՝ նրանց արժեքները մեծացնելով զույգ արժեք ունեցող տարրերից մեծագույնի արժեքի չափով
# import random
# A = []
# for i in range(1,101):
#     A.append(random.randrange(70))


# print(A)

# dict =  {}
# for i in A:
#     if A[i] not in dict:
#         dict[A[i]] = 0
#     else:
#         dict[A[i]]+=1

# count = 0
# for i in dict:
#     if dict[i]==2:
#         count+=1
# print(dict)
# print(count)
import random
# t = False
# x = [0,0]
# i = 0
# while i<=len(x)-3 and not t: #<10
#     if x[i]==0 and x[i+1]==0 and x[i+2]==0:
#         t = True
#     else:
#         i+=1

# print(t)
# n = int(input("n="))
# A = [random.randrange(30) for _ in range(n)]
# try:
#     n = int(input("n="))
#     X = [int(input(f"Enter {i+1} number for X vector: ")) for i in range(n)]
#     Y = [int(input(f"Enter {i+1} number for Y vector: ")) for i in range(n)]
#     flag = True
#     for elem in X:
#         if elem not in Y:
#             flag=False
#             break
    
#     if flag:
#         print(round((max(X)+max(Y))/2))
#     else:
#         print(round((min(X)*min(Y))**(1/2)))


#     arithmetic_mean = (max(X)+max(Y))//2
# except Exception as e:
#     print(e)


#գլխավոր անկյունագծից վերև կամ նրա վրա գտնվող այն տարրերի քանակը, որոնց ինդեքսների գումարը կենտ է
# n = int(input("n="))

# A = [[int(j) for j in input().split()] for i in range(n)]
# n = 3
# A = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# count = 0
# p = 1
# count = 0
# for i in range(n):
#     for j in range(0,i+1):
#         if A[i][j]%2!=0:
#             count+=1
#             p*=A[i][j]
# print(p)
# print(round(p**(1/count),2))
# def prime(n):
#     if n==1:
#         return False
#     flag = True
#     i = 2
#     while i<=n//2 and flag:
#         if n%i==0:
#             flag = False
#         i+=1
#     return flag


#     prime_l = []
#     for i in range(1,n):
#         for j in range(n-i, n):
#             if prime(A[i][j]):
#                 prime_l.append(A[i][j])

#     min_el = A[0][n-1]
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if A[i][j]<min_el:
#                 min_el = A[i][j]



#     max_el = max(prime_l)
#     for i in range(n):
#         A[i][i] = max_el
#         for j in range(n):
#             if i>j:
#                 A[i][j] = min_el


#     for i in A:
#         print(i)
# except Exception as e:
#     print(e)


# def perfect(el, n):
#     i = 0
#     perf_l = []
#     while i<n:
#         s = 0   
#         for j in range(1, el//2):
#             if el%j==0:
#                 s+=j
#         if s==el:
#             i+=1
#             perf_l.append(el)
#         el+=1
#     return perf_l
            

# try:
#     n = int(input("n="))
#     A = []
#     for i in range(n):
#         row = input().split()
#         if len(row)!=n:
#             raise Exception("not right")
#         for j in range(len(row)):
#             row[j] = int(row[j])
#         A.append(row)

#     max_el = A[0][n-1]
#     for i in range(1,n):
#         if A[i][n-i-1]>max_el:
#             max_el = A[i][n-i-1]
    
#     el = max_el+1
#     print(el)
#     print(perfect(el, n))
# except Exception as e:
#     print(e)

# A = []
# n = int(input("n="))
# for i in range(n):
#     row = input().split()
#     if len(row)!=n:
#         raise Exception("not right")
#     for j in range(len(row)):
#         row[j] = int(row[j])
#     A.append(row)

# for i in range(n):
#     max_el = max(A[i])
#     max_ind = A[i].index(max_el)
#     A[i][i], A[i][max_ind] = max_el, A[i][i]

# print("---------------------")
# for i in A:
#     for j in i:
#         print(j, end=' ')
#     print()
n = int(input("n="))
p = 1
p_i = 1
for i in range(1,16):
    p*=p_i
    p_i = 1
    for m in range(1, 7):
        var = i/(i+n*m)
        p_i*=var

print("product: ", p)