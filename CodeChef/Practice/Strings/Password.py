# cook your dish here
t=int(input())

while t>0:
    t-=1
    S=input()
        
        
    con1=con2=con3=con4=con5=0
    
    num=["0","1","2","3","4","5","6","7","8","9"]
    schar={ '@', '#', '%', '&', '?' }


    
    if len(S)>=10: 
        con5=1
    

    else:
        print("NO")
        continue
    
    
     
    for i in range(0,len(S)):
        if i==0 or i==len(S)-1:
            if S[i].islower(): con1=1
        
        else:
            if  (con1 and con2 and con3 and con4)!=1:
                if S[i] in num:
                    con3=1
                    
                elif S[i].islower(): 
                    con1=1
                    
                elif S[i].isupper():
                    con2=1
                
                
                    
                elif S[i] in schar:
                    con4=1
            
    if  (con1 and con2 and con3 and con4)==1:
        print("YES")
    
    else:
        print("NO")
            
            
            
            
            
            
            
            
                