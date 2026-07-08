def Numplus1(N):
    lst=list(N)
    carry=1
    
    for i in range(len(lst)-1,-1,-1):
        digit=int(lst[i])+1
        lst[i]=str(digit%10)
        if lst[i]!="0":
            carry=0
            break
    if carry:
        lst.insert(0,"1")
    return "".join(lst)
            
            

t=int(input())

while t>0:
    N=input()
    t-=1
    print(Numplus1(N))
    
    