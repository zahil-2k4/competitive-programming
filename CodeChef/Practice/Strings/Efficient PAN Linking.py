t = int(input())

while t > 0:
    
    s="0"+input()
    s=s[-2:]
    num=int(s)
    print(num%20)
    t-=1