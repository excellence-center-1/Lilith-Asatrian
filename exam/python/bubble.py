llist=[1,-19,60,24,98,50]

k=len(llist)
while(k>0):
    swapped_index=0
    for i in range(k-1):
        if llist[i]>llist[i+1]:
            tmp=llist[i]
            llist[i]=llist[i+1]
            llist[i+1]=tmp
            swapped_index=i
    k=swapped_index+1
    if swapped_index == 0:
        break

print(llist)

        
        

    