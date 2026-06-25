t=int(input())

while t>0:
    t-=1
    n=int(input())
    nums=list(map(int,input().split()))

    longest=[]
    lis=[]
    z=2
    while z>0:
        z-=1
        for i in range(0,len(nums)):
            for x in range(0,len(longest)):
                if longest[x]+1==nums[i] or longest[x]-1==nums[i]:
                    longest.append(nums[i])
                    break
            for y in range(0,len(lis)):
                    if lis[y]+1==nums[i] or lis[y]-1==nums[i]:
                        lis.append(nums[i])
                        break
                    
            
                    



            if len(longest)==0:
                    longest.append(nums[i])

            else:
                if len(lis)==0:
                    lis.append(nums[i])

        

            if len(longest)>len(lis):
                lis.clear()
            
            elif len(longest)==len(lis):
                print("same")
            else:
                
                longest.clear()
                longest=list(lis)
                lis.clear()
        
    count=(list(set(longest)))
    print(count)
    print(len(count))       
             
    

