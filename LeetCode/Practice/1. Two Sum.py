class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        j=0
        k=1
        while j<len(nums)-1:
            
            for i in range(k,len(nums)):
                if  nums[j]+nums[i]==target:
                    out=[j,i]
                    return out
            
            j+=1
            k+=1
