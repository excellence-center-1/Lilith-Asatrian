#INSERTION
llist=[-63,-78,0,2,1,19,16]

for i in range(1,len(llist)):
    key = llist[i]
    j = i-1
    while key<llist[j] and j>=0:
        llist[j+1] = llist[j]
        j-=1
    llist[j+1] = key

print(llist)
    
