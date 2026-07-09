# def isAnagram(s, t):
#     lst=list(s)
#     for i in t:
#         if i in lst:
#             lst.remove(i)                 method 1
        
#         else:
#             return 0
#     return 1
def isAnagram(s, t):
    freq_s={}
    freq_t={}

    for i in s:
        if i in freq_s:
            freq_s[i]+=1
            
        else:
            freq_s[i]=1
            
    for i in t:                             #method 2
        if i in freq_t:
            freq_t[i]+=1
            
        else:
            freq_t[i]=1
            
    if freq_s==freq_t:
        return 1
    else:
        return 0
        
# def isAnagram(s, t):
#     if sorted(s)==sorted(t):
#         return 1                          method 3
#     else:
#         return 0
    
