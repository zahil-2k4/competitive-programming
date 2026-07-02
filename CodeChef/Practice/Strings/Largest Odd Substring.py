def findLargestOddSubstring(num):
    pointer=-1
    for i in range(len(num)):
        if int(num[i])%2!=0:
            pointer=i
            
    if pointer==-1:
        return pointer
    else:
        return num[:pointer+1]
    

