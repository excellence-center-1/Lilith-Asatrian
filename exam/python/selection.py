llist=[-63,-78,0,2,1,19,16]

for i in range(len(llist)):
    min=llist[i]
    min_index=i
    for j in range(i+1,len(llist)):
        if(llist[j]<min):
            min=llist[j]
            min_index=j
    tmp=llist[i]
    llist[i]=llist[min_index]
    llist[min_index]=tmp

print(llist)