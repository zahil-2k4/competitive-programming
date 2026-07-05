def findMaxConsecutiveOnes(nums):
    maxcount=0
    count=0
    for i in range(0,len(nums)-1):
        if nums[i]==0:
           count=0
        if nums[i]==1 and nums[i+1]==1:
            if count==0:
                count=2
            else:
                count+=1
        
        if count>maxcount:
            maxcount=count
    if maxcount==0 and 1 in nums:
        maxcount=1
        
    return maxcount
        
    