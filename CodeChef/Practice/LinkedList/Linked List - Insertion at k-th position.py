class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_after_k(self,value,k):
        new_node=Node(value)

        if self.head==None:
            self.head=new_node
            return 
        else:
            current=self.head
            for i in  range(k-1):
                current=current.next
            new_node.next=current.next
            current.next=new_node
    def print_values(self):
        if self.head==None:
            return "LL is empty"
        else:
            current=self.head
            while current:
                print(current.value,end=" ")
                current=current.next
            print()
            
N=int(input("No of elements in LL"))
x,k=map(int,input("Enter the number and position to insert the element").split())
lst=list(map(int,input("Enter the elements of LL").split()))

LL=LinkedList()

for i in range(N):
    LL.insert_after_k(lst[i],i)

LL.print_values()

LL.insert_after_k(x,k)
LL.print_values()