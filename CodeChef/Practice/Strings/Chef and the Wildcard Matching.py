# cook your dish heret = int(input())


t = int(input())

while t > 0:
    x = input()
    y = input()
    t -= 1
    out=1
    
    for i in range(len(x)):
        if x[i]!="?" and y[i]!="?":
            if x[i]!=y[i]:
                out=0
                break
                
            
                
    print("Yes") if out else print("No")   