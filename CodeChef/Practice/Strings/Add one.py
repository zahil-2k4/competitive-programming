def Numplus1(N):
    
    flag=0
    pointer=1
    for i in range(len(N)-1,-1,-1):
        lastbit=int(N[i])
        if N[i]=="9":
            flag=1
            lastbit="0"
            N=N[:-pointer]+lastbit*pointer
            pointer+=1
            if i==0:
                return "1"+N
            
            
            
        else:
            lastbit=str(lastbit+1)
            N=N[:-pointer]+lastbit
            if flag==1:N+="0"*(pointer-1)
            return  N
            

t=int(input())

while t>0:
    N=input()
    t-=1
    print(Numplus1(N))
    
    