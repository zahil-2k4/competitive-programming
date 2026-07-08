def reverseWords(s: str) -> str:
    lst=s.split()
    revstr=""
    for i in range(len(lst)-1,-1,-1):
        revstr+=lst[i]+" "
    
    return revstr
        
    