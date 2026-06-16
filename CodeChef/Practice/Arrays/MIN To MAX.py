class Solution:
    def count_non_minimum(self, nums):
        M=min(nums)
        count=0
        for i in nums:
            if i>M:
                i=M
                count+=1
        
        return count
