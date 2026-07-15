def peek():
    global top
    if top==-1:
        print("Stack empty")
    else:
        print("arr[top]")
              
def is_full():
    if top>=max_size-1:
        return True
    else:
        return False
        
def is_empty():
    if top==-1:
        return True
    else:
        return False
