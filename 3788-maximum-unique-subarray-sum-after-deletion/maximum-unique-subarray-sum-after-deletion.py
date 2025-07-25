import math

class Solution(object):
  def maxSum(self, nums):
    if not nums:
      return 0

    # Find all unique numbers in the input array.
    unique_nums = set(nums)

    # Sum only the unique numbers that are positive.
    max_sum = 0
    for num in unique_nums:
      if num > 0:
        max_sum += num

    # If max_sum is 0, it means there were no unique positive numbers.
    # In this case, the result must be the largest element in the original array.
    if max_sum == 0:
      return max(nums)
    
    return max_sum
