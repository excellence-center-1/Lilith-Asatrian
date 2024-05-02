class Vector: 
    def __init__(self):
        self.myVector=[]
        self.size=0
    
    def vec_size(self):
        return self.size
    
    def push_back(self, value):
        self.myVector.append(value)
        self.size+=1
    
    def top(self):
        return self.myVector[-1]
    
    def popf(self):
        if self.size == 0:
            return None
        else:
            popped_element=self.myVector.pop()
            self.size-=1
            return popped_element

    def insert(self, index, value):
        if index>self.size:
            return None
        temp=self.myVector[index]
        self.myVector[index]=value
        for i in range (index+1, self.size):
            next_val=self.myVector[i]
            self.myVector[i]=temp
            temp=next_val
        self.myVector.append(temp)
        self.size+=1
        
    def delete(self, index):
        if(index>=self.size): 
            return None
        for i in range(index, self.size-1):
            self.myVector[i]=self.myVector[i+1]
        self.myVector.pop()
        self.size-=1
    
    # def find(self, elem):
    #     for i in range(self.size):
    #         if elem==self.myVector[i]:
    #             return i
    #     return -1
    def find(self, elem):
        try:
            return self.myVector.index(elem)
        except ValueError:
            return "Element not found"
vec=Vector()

vec.push_back(10)
vec.push_back(20)
vec.push_back(63)

print("Top element: ",vec.top())

print("Popped element: ",vec.popf())
# for elem in vec.myVector:
#     print(elem)
vec.insert(1,18)
vec.delete(0)
print("Found element at index: ",vec.find(63))
print("The list: ", [element for element in vec.myVector])