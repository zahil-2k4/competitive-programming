t = int(input())

while t > 0:
    n = int(input())
    S = input()
    server='A'
    Alice=0
    Bob=0
    for i in range(len(S)):
        if S[i]==server:
            if server=="A":
                Alice+=1
            else:
                Bob+=1
        else:
            server=S[i]
    print(Alice,Bob)
    
    
    t -= 1
