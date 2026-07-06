t = int(input())

while t > 0:
    s = input()
    num=0
    for i in s:
        num=num*10+(ord(i)-ord("0"))
    if num<20:
        print(num)
    else:
        print(num%20)
    t -= 1
