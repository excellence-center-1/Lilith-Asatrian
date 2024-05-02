import math
def jump_search(llist, elem):
    i=0
    m=int(math.sqrt(len(llist)))
    while i<len(llist) and llist[i]<elem:
        if llist[i]==elem:
            return i
        i+=m

    if i>len(llist):
        return -1

    for i in range(i-m, i):
        if llist[i]==elem:
            return i
        
llist=[1,3,5,6,7]
print(jump_search(llist, 8))

