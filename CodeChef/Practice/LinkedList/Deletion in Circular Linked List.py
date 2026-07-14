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
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.tail.next = self.head

    def deleteNode(self, value):
        # If there is only one element and it is the value to be deleted, remove it
        if self.head == self.tail and self.head.value == value:
            self.head = None
            self.tail = None
            return

        # if the target is at head set head to second element and set tail's next to the new head
        iter = self.head
        if self.head.value == value:
            self.head = self.head.next
            self.tail.next = self.head
            return

        while iter.next is not None and iter != self.tail:
            if iter.next.value == value:
                iter.next=iter.next.next
                break
            iter = iter.next
            