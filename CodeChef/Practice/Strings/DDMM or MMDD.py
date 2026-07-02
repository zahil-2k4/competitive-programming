t = int(input())

while t > 0:
    s = input()
    
    
    if int(s[0:2])<=12:
        if int(s[3:5])<=12:
            print("BOTH")
        else:
            print("MM/DD/YYYY")
    
    
    else:
        print("DD/MM/YYYY")
    
    
    t -= 1
