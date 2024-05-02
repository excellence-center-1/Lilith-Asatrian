# def reverseString(str):
#     newstr=""
#     for i in range(len(str)-1, -1, -1):
#         newstr+=str[i]
    
#     return newstr

# print(reverseString("garik"))

# def reverseString(str):
#     llist=[]
#     for i in range(len(str)-1, -1, -1):
#         llist.append(str[i])
#     return ''.join(llist)



#easiest
def reverseString(str):
    return str[::-1]

print(reverseString("garik"))