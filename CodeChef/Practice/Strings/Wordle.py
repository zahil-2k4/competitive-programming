t=int(input())

while t>0:
    S=input()
    T=input()
    M=""
    
    for i,j in zip(S,T):
        if i==j:
            M+="G"
        else:
            M+="B"
    
    print(M)
   
    t-=1