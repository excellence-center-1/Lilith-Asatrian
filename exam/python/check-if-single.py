def merge_sorted_lists(ll1, ll2):
    l1=0
    l2=0
    ll=[]

    while l1<len(ll1) and l2<len(ll2):
        if ll1[l1]<ll2[l2]:
            ll.append(ll1[l1])
            l1+=1
        else:
            ll.append(ll2[l2])
            l2+=1
    ll.extend(ll1[l1::])
    ll.extend(ll2[l2::])
    return ll

ll1=[1,3,4,5,9]
ll2=[2,7,8,11,13,15]

print(merge_sorted_lists(ll1, ll2))