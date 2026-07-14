class Node:
    def __init__(self,value):
        self.value=value
        self.next=None 

class LinkedList():
    def __init__(self):
        self.head=None
        self.tail=None

    def insertAtEnd(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node

    def deleteNode(self,value):
        if self.head.value==value:
            self.head=self.head.next 
        else:
            current=self.head
            while current.next:
                
                if current.next.value==value:
                    current.next=current.next.next
                    return
                current=current.next
                