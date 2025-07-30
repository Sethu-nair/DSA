class Solution(object):
    def longestSubarray(self, nums):
        maxnum=max(nums)
        currentmax=0
        finalmax=0
        for i in nums:
            if i==maxnum:
                currentmax+=1
                finalmax=max(finalmax,currentmax)
            else:
                currentmax=0
        return finalmax


            

