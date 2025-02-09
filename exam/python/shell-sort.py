llist =[9,8,3,7,5,6,4,1]

def ShellSort(llist):
    N = len(llist)
    interval = N//2
    while interval>0:
        for i in range(interval, N):
            key = llist[i]
            j = i-interval
            while key<llist[j] and j>=0:
                llist[j+interval] = llist[j]
                j-=interval

            llist[j+interval] = key
        interval//=2

    return llist

print("Shell sort: ", ShellSort(llist))
