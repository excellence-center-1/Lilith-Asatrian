llist = [5,-96,152,36,9]
# for i in range(len(llist)-1):
#     for j in range(i+1, len(llist)):
#         if(llist[i]>llist[j]):
#             temp = llist[i]
#             llist[i] = llist[j]
#             llist[j] = temp

# print(llist)

# for i in range(len(llist)-1, 0,-1):
#     for j in range(i-1, -1, -1):
#         if(llist[i]<llist[j]):
#             temp = llist[i]
#             llist[i] = llist[j]
#             llist[j] = temp

for i in range(1,len(llist)):
    k = i-1
    while k>=0 and llist[i]<llist[k]:
        llist[i], llist[k] = llist[k], llist[i]
        --k

print(llist)