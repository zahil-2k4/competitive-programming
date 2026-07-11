class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def insert_front(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node

    def get_head(self):
        if self.head==None:
            return -1
        else:
            return self.head.value
        
list=LinkedList()
list.insert_front(5)
list.insert_front(4)
list.insert_front(3)

headval=list.get_head()
print(headval)