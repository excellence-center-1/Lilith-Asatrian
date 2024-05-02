llist=[-63,-78,0,2,1,19,16]

for i in range(1,len(llist)):
    for j in range(i, 0, -1):
        if(llist[j]>llist[j-1]):
            break
        tmp=llist[j]
        llist[j]=llist[j-1]
        llist[j-1]=tmp

print(llist)