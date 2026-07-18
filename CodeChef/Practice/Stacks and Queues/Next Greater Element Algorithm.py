N=int(input())
arr=list(map(int,input().split()))

nge=[-1]*N
stack=[]

for i in range(N-1,-1,-1):
    flag=0
    while flag==0:
        if not stack:
            stack.append(arr[i])
            nge[i]=-1
            flag=1
        
        else:
            if arr[i]<stack[-1]:
                nge[i]=stack[-1]
                stack.append(arr[i])
                flag=1
            
            elif arr[i]>stack[-1]:
                stack.pop()
print(*nge)