t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
    streak=0
    comp=0
    for i in range(len(a)):
        if a[i]==0 or b[i]==0:
            if comp>streak:
                streak=comp
            comp=0
        else:
            comp+=1
    if comp>streak:
        streak=comp
    print(streak)