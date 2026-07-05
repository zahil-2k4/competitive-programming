def string_to_number(s):
    num=0
    leng=len(s)-1
    for i in s:
        num+=(ord(i)-ord("0"))*10**leng
        leng-=1
    return num


