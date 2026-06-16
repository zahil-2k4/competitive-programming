t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    
    # Your code goes here
    max1=0
    max2=0
    for i in a:
        if i>max1:
            max2=max1
            max1=i
        elif i>max2 and i!=max1:
            max2=i
    
    print(max1+max2)