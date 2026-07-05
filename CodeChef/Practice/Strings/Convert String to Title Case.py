

def ToTittleCase(S):
    words=S.split()
    for i in range(len(words)):
        if words[i].isupper():
            continue
        
        else:
            lst=list(words[i])
            lst[0]=lst[0].upper()
            for z in range(1,len(lst)):
                if lst[z].isupper():
                    lst[z]=lst[z].lower()
                
            
            new="".join(lst)
            words[i]=new
    
    out=" ".join(words)
    
    return out


t=int(input())
while t>0:
    t-=1
    S=input()
    print(ToTittleCase(S))    
    
    
    
    