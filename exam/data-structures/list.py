class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def push_front(self, value):
        if not isinstance(value, Node):
            value = Node(value)
        if self.head == None:
            self.head=value
        else:
            next_val=self.head
            self.head=value
            self.head.next=next_val
            next_val.prev=self.head

    def push_back(self, value):
        if not isinstance(value, Node):
            value = Node(value)
        if self.head is None:
            self.head=value
        else:
            curr_elem=self.head
            while curr_elem.next:
                curr_elem=curr_elem.next
            curr_elem.next=value   
            value.prev=curr_elem

    def insert(self, value, ind):
        if not isinstance(value, Node):
            value = Node(value)
        if self.head is None:
            self.head=value
            return
        i=0
        curr_elem=self.head
        while i<ind and curr_elem.next:
            i+=1
            curr_elem=curr_elem.next
        if curr_elem.next is None:
            curr_elem.next=value   
            value.prev=curr_elem
            return
        temp=curr_elem.prev
        curr_elem.prev=value
        value.prev=temp
        value.next=curr_elem
        temp.next=value
    def __str__(self):
        output=""
        curr_elem=self.head
        while(curr_elem != None):
            if(curr_elem.next != None):
                output+=str(curr_elem.data)+"->"
            else:
                output+=str(curr_elem.data)
            curr_elem=curr_elem.next
        if output=="":
            output+="There are no elements in your list"
        return output
    
    def pop_front(self):
        if self.head:
            if self.head.next:
                self.head.next.prev=None
                self.head=self.head.next
                return
            self.head=None

    def pop_back(self):
        curr_el=self.head
        while curr_el.next:
            curr_el=curr_el.next   
        curr_el.prev.next=None

    def find(self, value):
        try:
            i=0
            curr_el=self.head
            while curr_el:
                if curr_el.data == value:
                    return i
                else:
                    i+=1
                    curr_el=curr_el.next
        except ValueError:
            return "Element is not found"
        
    def reverse(self):
        curr_el=self.head
        while curr_el.next:
            curr_el=curr_el.next
        self.head=curr_el
        while curr_el:
            curr_el.next, curr_el.prev=curr_el.prev, curr_el.next
            curr_el=curr_el.next
            
myList=DoublyLinkedList()
myList.push_front(51)
print(myList)
myList.push_front(12)
print(myList)
myList.push_back(19)
print(myList)
myList.insert(18,1)
print(myList)
myList.insert(25,4)
print(myList)
myList.pop_front()
print(myList)
myList.pop_back()
print(myList)
myList.reverse()
print(myList)
print(myList.find(51))