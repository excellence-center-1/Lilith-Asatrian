def merge(ll1, ll2):
    i = 0
    j = 0
    sorted = []
    while i<len(ll1) and j<len(ll2):
        if ll1[i]<ll2[j]:
            sorted.append(ll1[i])
            i+=1
        else:
            sorted.append(ll2[j])
            j+=1

    sorted.extend(ll1[i:])
    sorted.extend(ll2[j:])
    
    return sorted

def mergeSort(llist):
    if(len(llist)>1):
        left_side = llist[:len(llist)//2]
        right_side = llist[len(llist)//2:]
        ll1 = mergeSort(left_side)
        ll2 = mergeSort(right_side)
        return merge(ll1, ll2)
    return llist

llist = [6,5,12,10,9,1]
print("Merged list", mergeSort(llist))
