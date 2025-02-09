
def partition(llist, low, high):
    piv_ind = low
    i = low+1
    j = high
    while True:
        while i<=j and llist[i]<=llist[piv_ind]:
            i+=1

        while i<=j and llist[j]>=llist[piv_ind]:
            j-=1

        if i<=j:
            llist[i], llist[j] = llist[j], llist[i]
        else:
            break
    llist[piv_ind], llist[j] = llist[j], llist[piv_ind]

    return j

def QuickSort(llist, low, high):
    if low<high:
        pivot_index = partition(llist, low, high)
        QuickSort(llist, low, pivot_index-1)
        QuickSort(llist, pivot_index+1, high)
    return llist

llist = [10,16,8,12,15,6,13,9,15]
print("Quicked sort list: ", QuickSort(llist, 0, len(llist)-1))




        
        
        