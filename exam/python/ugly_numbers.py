# def nth_ugly(n):
#     ugly_numbers = [1]*n
#     index_2, index_3, index_5 = 0, 0, 0
#     for i in range(1, n):
#         next_2 = ugly_numbers[index_2]*2
#         next_3 = ugly_numbers[index_3]*3
#         next_5 = ugly_numbers[index_5]*5

#         ugly_numbers[i] = min(next_2, next_3, next_5)
        
#         if ugly_numbers[i]==next_2:
#             index_2+=1
#         elif ugly_numbers[i]==next_3:
#             index_3+=1
#         elif ugly_numbers[i] == next_5:
#             index_5+=1

#     return ugly_numbers[n-1]

# print(nth_ugly(6))

def nth_ugly(n):
    ugly_numbers = []
    ugly_numbers.append(1)#[1]
    flag = False
    index = 1
    curr = 2
    while index<n:
        for i in range(2, curr+1):
            if curr%i==0:
                if i==2 or i==3 or i==5:
                    flag = True
                else:
                    s = 0
                    for j in range(1, i+1):
                        if i%j==0:
                            s+=1
                    if s==2:
                        flag = False
        if flag:
            ugly_numbers.append(curr)
            index+=1
        curr+=1
    return ugly_numbers


print(nth_ugly(11))