def shortestPalindrome(S):
    if S==S[::-1]:
        return S
    
    for i in range(len(S)-1,0,-1):
        if S[i]==S[0]:
            new_s=S[0:i+1]
            if new_s==new_s[::-1]:
                return S[:i:-1]+new_s+S[i+1:]

    
    new_s=S[:0:-1]+S
    return new_s
    
t=int(input())
while t>0:
    t-=1
    S=input()
    print(shortestPalindrome(S))