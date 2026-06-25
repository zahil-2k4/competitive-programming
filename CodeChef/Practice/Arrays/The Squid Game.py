t=int(input())


while t>0:
    n=int(input())
    a=list(map(int,input().split()))
    
    money=0
    smalest=min(a)
    for i in range(0,len(a)):
        money+=a[i]
    money-=smalest
    print(money)
    t-=1