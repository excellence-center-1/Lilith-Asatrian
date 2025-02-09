class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        llist = []
        current = self
        while current:
            llist.append(str(current.val))
            current=current.next
        result=" ".join(llist)
        return result



dummy = ListNode()
l1 = ListNode(3, ListNode(4, ListNode(5)))
l2 = ListNode(6, ListNode(8, ListNode(9)))
curr = dummy
carry = 0

while l1 or l2 or carry:
    firstdigit = l1.val if l1 else 0 
    seconddigit = l2.val if l2 else 0
    number = firstdigit+seconddigit+carry
    curr.next = ListNode(number%10)
    carry=number//10 #grel ei carry+=number//10
    curr = curr.next
    if l1:
        l1 = l1.next
    if l2:
        l2 = l2.next

axper = dummy.next
print(axper)
