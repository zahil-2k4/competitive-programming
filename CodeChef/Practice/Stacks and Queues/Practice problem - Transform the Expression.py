arr=[0]*100
top=-1

def push(element):
    global top
    top+=1
    arr[top]=element
    
def pop():
    global top 
    x=arr[top]
    top-=1
    return x

def algebra_to_RPN(S):
    out=''
    ret=''
    for i in S:
        match i:
            case "(":
                push(i)      
            
            case ")":
                
                while ret!="(":
                    out=out+ret
                    ret=pop()
                ret=''
                    
            case _ if i.islower():
                out+=i
            
            case _:
                push(i)
                    
                
    return out 

t=int(input())

while t>0:
    t-=1
    s=input()
    print(algebra_to_RPN(s))
    
                
                    
                