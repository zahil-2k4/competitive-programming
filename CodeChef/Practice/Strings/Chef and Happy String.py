def emotion(S):
    count=0
    for i in range(len(S)):
        if count>2:
            return "Happy"
        if S[i] in {'a','e','i','o','u'}:
            count+=1
        else:
            count=0
    if count>2:
        return "Happy"
    else:
        return "Sad"

t = int(input())

while t > 0:
    s = input()
    print(emotion(s))
    
    t -= 1
