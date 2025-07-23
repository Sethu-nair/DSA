class Solution(object):
    def longestConsecutive(self, nums):
        if(len(nums)==0):
            return 0
        nums.sort()
        count=1 
        longest =0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]-nums[i-1]==1:
                count+=1
            else:
                longest=max(count, longest)
                count=1
        return max(longest, count)




        