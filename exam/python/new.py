def merge(left_llist, right_llist):
    i = 0
    j = 0
    new_llist = []
    while i < len(left_llist) and j < len(right_llist):
        if left_llist[i] < right_llist[j]:
            new_llist.append(left_llist[i])
            i += 1
        else:
            new_llist.append(right_llist[j])
            j += 1
    
    while i < len(left_llist):
        new_llist.append(left_llist[i])
        i += 1
    
    while j < len(right_llist):
        new_llist.append(right_llist[j])
        j += 1
    
    return new_llist

def merge_sort(llist):
    if len(llist) <= 1:
        return llist
    
    mid_point = len(llist) // 2
    left_list = llist[:mid_point]
    right_list = llist[mid_point:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return merge(left_list, right_list)

llist = [-63, -78, 0, 2, 1, 19, 16]
print(merge_sort(llist))
