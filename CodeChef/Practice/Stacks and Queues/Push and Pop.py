max_size=100
arr=[0]*100
top=-1

def push(element):
    global top 
    if top>=max_size-1:
        return "Stack is full"
    else:
        top+=1
        arr[top]=element
def pop():
    global top
    if top==-1:
        return "Stack is empty"
    else:
        print(f"Element {arr[top]} has been popped")
        top-=1


