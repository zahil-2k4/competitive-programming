n=int(input())
arr=list(map(int,input().split()))
stack=[]
nse=[0]*n

for i in range(n-1,-1,-1):
    flag=0
    while flag==0:
        if not stack:
            nse[i]=-1
            stack.append(arr[i])
            flag=1
            
        else:
            if arr[i]>stack[-1]:
                nse[i]=stack[-1]
                stack.append(arr[i])
                flag=1
            
            else:
                stack.pop()
                
            
print(*nse)        
