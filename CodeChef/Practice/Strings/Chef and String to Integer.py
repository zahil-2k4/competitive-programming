def myAtoi(s: str) -> int:
    digit=neg=loop=sign=num=0   
 
    while digit==0 and loop<len(s):
        if s[loop]=="0" or s[loop]==" ":
            loop+=1
            continue
        elif  s[loop].isdigit():
            digit=1
            continue
        elif s[loop]=="-":
            if sign==0:
                neg=sign=1
                loop+=1
            else:
                return 0 
        elif s[loop]=="+":
            if sign==0:
                sign=1
                loop+=1
            else:
                return 0
        
        else:
            return 0
        
        
    while digit==1 and loop<len(s):
        if s[loop].isdigit()==False:
            break
        
        else:
            num=num*10+(ord(s[loop])-ord("0"))
            loop+=1
            
            
    if neg==1:num*=-1
        
    
           
    if num>2147483647:
        return 2147483647
    elif num<-2147483648:
        return -2147483648        
            
    return num         
            
            
            