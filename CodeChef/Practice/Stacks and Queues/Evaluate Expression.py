arr=[0]*100


def push(element):
    global top
    top+=1
    arr[top]=element
    
def pop():
    global top 
    if top==-1:
        return "Empty"
    x=arr[top]
    top-=1
    return x






t=int(input())
while t>0:
    t-=1
    top=-1
    N=int(input())
    S=input()
    out=0
    for i in S:
        match i:
            case _ if i.isdigit():
                push(i)
                
            case '*'|'-'|'+'|'/'|'^':
                
                b = int(pop())
                a = int(pop())
                
                if i == '+':
                    out=(a + b)
                elif i == '-':
                    out=(a - b)
                elif i == '*':
                    out=(a * b)
                elif i == '/':
                    out=(a / b)
                push(out)
    print(out)