class HashTable:
    def __init__(self, size):
        self.size=size
        self.llist=[[] for i in range(self.size)]

    def __str__(self):
        output=""
        for i in range(self.size):
            output+=str(self.llist[i])
        return output

    # def add_elem(self, key, value):
    #     hashed_value=hash(key)%self.size
    #     self.llist[hashed_value].append((key, value))
    def add_elem(self, key, value):
        hashed_value=hash(key)%self.size
        for i, (existing_key, _) in enumerate(self.llist[hashed_value]):
            if existing_key==key:
                self.llist[hashed_value][i]=(key, value)
                return
        self.llist[hashed_value].append((key, value))
    
    def update_elem(self, key, value):
        hashed_value=hash(key)%self.size
        try:
            if self.llist[hashed_value]:
                self.llist[hashed_value]=(key,value) 
                return
        except ValueError:
            return "No suc key in your list"  

    def get_elem(self, key):
        hashed_value=hash(key)%self.size
        return self.llist[hashed_value]

hashtable=HashTable(256)
hashtable.add_elem("lilik", "esimvortexic")
hashtable.add_elem("lilik", "vanadzor")
hashtable.update_elem("lilik", "erevan")
print(hashtable)
print(hashtable.get_elem("lilik"))
