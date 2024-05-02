my_llist=[
    [1,23], 
    [59,3,6,9], 
    [54,2,6,9]
]
# new_ll=[]
# for i in my_llist:
#     for j in i:
#         new_ll.append(j)
# print(new_ll)

new_ll=[j for i in my_llist for j in i]
print(new_ll)