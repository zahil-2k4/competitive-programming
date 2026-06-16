T=int(input())

while T>0:
    T-=1
    ary=list(map(int,input().split()))
    N=ary[0]
    K=ary[1]

    los=list(map(int,input().split()))
    
    count=0
    for i in los:
        if i>K:
            count+=1
    
    print(count)