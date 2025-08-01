class Solution:
    def maxSubArray(self, nums):
        max_sum = current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)  # Extend or start new subarray
            max_sum = max(max_sum, current_sum)        # Update max seen so far

        return max_sum

        