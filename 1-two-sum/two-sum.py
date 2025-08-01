class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i in range(len(nums)):
            if target-nums[i] in d:
                return i,d[target-nums[i]]
            else:
                d[nums[i]]=i

        