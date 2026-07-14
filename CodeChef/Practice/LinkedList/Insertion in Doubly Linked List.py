class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_index(self, index, value):
        # Complete this function
        new_node=Node(value)
        
        if index==0:
            if self.head is None:
                self.head=new_node
            else:
                new_node.next=self.head
                self.head.prev=new_node
                self.head=new_node
        else:
            current=self.head
            for i in range(index-1):
                current=current.next
            
            store=current.next
            current.next=new_node
            new_node.prev=current
            new_node.next=store
            
    def print_values(self):
        current = self.head
        while current is not None:
            print(current.value, end=' ')
            current = current.next
        print()

