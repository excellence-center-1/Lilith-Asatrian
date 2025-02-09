llist = [1,2,-987, -8,12,3,4,5]

def selection(myList):
    for i in range(len(myList)):
        min = myList[i]
        minindex = i
        for j in range(i+1, len(myList)):
            if min>myList[j]:
                min = myList[j]
                minindex = j
        myList[i], myList[minindex] = myList[minindex], myList[i]

    return myList

print("Selection", selection(llist))
