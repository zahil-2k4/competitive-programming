t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
# Your code goes here
    om=0
    ommax=0
    addy=0
    addymax=0
    
    for i in a:
        if i!=0:
            om+=1
        else:
            ommax=max(om,ommax)
            om=0
            
    for i in b:
        if i!=0:
            addy+=1
        else:
            addymax=max(addy,addymax)
            addy=0
         
         
    ommax=max(om,ommax)     
    addymax=max(addy,addymax)
    
    
    
            
    if ommax>addymax:
        print("OM")
    elif addymax>ommax:
        print("Addy")
    else:
        print("Draw")