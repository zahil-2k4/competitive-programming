# arr=list(map(int,input().split()))
# print(arr)
# maxarea=0

# for i in range(len(arr)):
#     container=[arr[i]]
#     area=arr[i]                                         BRUTE FORCE METHOD FOR TESTING 
#     if area>maxarea:
#         maxarea=area         
#     for j in range(i+1,len(arr)):  
#             container.append(arr[j])
#             area=(min(container))*(len(container))
#             if area>maxarea:
#                 maxarea=area
# print(maxarea)


A=list(map(int,input().split()))
print(A)

N=len(A)
NSL=[-1]*N
NSR=[N]*N
    
#NSL
stack=[]
for i in range(N):
    while stack and A[stack[-1]]>=A[i]:
        stack.pop()
    if stack:
         NSL[i]=stack[-1]       
    stack.append(i)
  
print(NSL)
stack.clear()   

#NSR
for i in range(N-1,-1,-1):
    while stack and A[stack[-1]]>=A[i]:
        stack.pop()

    if stack:
        NSR[i]=stack[-1]  
    stack.append(i)  

print(NSR)

area=[0]*N
for i in range(N):
    width=(NSR[i] - 1) - (NSL[i] + 1) + 1
    area[i]=width*A[i]
maxarea=max(area)
print(maxarea)