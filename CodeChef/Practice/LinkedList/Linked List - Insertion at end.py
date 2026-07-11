class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

    def insert_end(self,value):
        new_node=Node(value)

        if self.head==None:
            self.head=new_node
            return 
        else:
            current=self.head
            while current.next:
                current=current.next 

            current.next=new_node

    def get_last_value(self):
        if self.head==None:
            return -1
        else:
            current=self.head
            while current.next:
                current=current.next

            return current.value 
        

list=LinkedList()        
N=int(input("Enter the length of LL"))

for i in range(N):
    list.insert_end(int(input("Enter the value to be inserted")))

print("Last value",list.get_last_value())
