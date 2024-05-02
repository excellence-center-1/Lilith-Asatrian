def partition(llist, low, high):  
    j=low
    pivot=llist[high]

    for i in range(low, high):
        if llist[i]<pivot:
            llist[i], llist[j] = llist[j], llist[i]
            j+=1
    (llist[j], llist[high])=(llist[high], llist[j])
    return j

def quick_sort(llist, low, high):
    if low<high:
        pivot_index=partition(llist, low, high)
        quick_sort(llist, low, pivot_index-1)
        quick_sort(llist, pivot_index+1, high)

    return llist

llist=[6,5,12,10,9,1]
print(quick_sort(llist, 0, len(llist)-1))