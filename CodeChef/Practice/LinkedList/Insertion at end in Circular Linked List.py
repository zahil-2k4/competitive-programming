class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtEnd(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head=new_node
            self.tail=new_node
            
        else:
           self.tail.next=new_node
           self.tail=new_node
           new_node.next=self.head
