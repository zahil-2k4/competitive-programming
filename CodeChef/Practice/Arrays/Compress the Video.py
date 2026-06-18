T=int(input())

for x in range(0,T):
    N=int(input())
    aray=list(map(int,input().split()))
    
    
    group=1
    for i in range(1,len(aray)):
        if aray[i]!=aray[i-1]:
            group+=1
            
    
    print(group)