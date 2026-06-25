t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    min=d[0]
    flag=1
    for i in range(1,len(d)):
        if d[i]<min:
            flag=0;
            break;
        else:
            min=d[i]
    if flag==1:
        print("Yes")
    else:
        print("No")
    
    t -= 1