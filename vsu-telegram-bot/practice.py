# try:
#     n = int(input("n="))
#     A = []
#     for i in range(n):
#         row = input().split()
#         if(len(row)!=n):
#             raise Exception("The length of row must be equal to n!")
#         for j in range(len(row)):
#             row[j] = int(row[j])
#         A.append(row)
    
#     min_1 = A[1][n-1]
#     min_2 = A[1][n-1]
#     for i in range(2, n):
#         for j in range(n-i, n):
#             if A[i][j]<min_1:
#                 min_1, min_2 = A[i][j], min_1
#             elif A[i][j]<min_2:
#                 min_2 = A[i][j]

#     print("min_1", min_1)
#     print("min_2", min_2)
        
# except Exception as e:
#     print("Enexpected exception occured: ", e)

# x = [2,1,5,6,2,22,3,4] #[1,2,2,3,4,5,6,22]
# y = []
# n = 8
# key = x[0]
# x.sort()
# i = 0
# while x[i]<key:
#     y.append(x[i])
#     i+=1
# while x[i]==key:
#     y.append(x[i])
#     i+=1
# y.append(x[i:])
# print(y)

# def prime(n):
#     if n==1:
#         return False
#     for i in range(2,n//2+1):
#         if n%i == 0:
#             return False
#     return True
        
# def prime_sec(n):
#     flag = True

#     while flag:

# print(prime(27))

n = int(input("n="))
m = int(input("m="))


# A = [0]*n

# for i in range(n):
#     A[i] = [0]*m

# A[0][1] = 5



# A = [[0]*m for i in range(n)]


A = []
for i in range(n):
    A.append([0]*m)

for i in A:
    print(i)