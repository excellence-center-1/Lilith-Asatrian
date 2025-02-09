llist = [1,2,-987, -8,12,3,4,5]

def bubble_sort(llist):
    for i in range (len(llist)):
        flag = True
        for j in range(len(llist)-i-1):
            if(llist[j]>llist[j+1]):
                flag = False
                llist[j], llist[j+1] = llist[j+1], llist[j]
        if(flag):
            return llist

print("llist", bubble_sort(llist))
                


