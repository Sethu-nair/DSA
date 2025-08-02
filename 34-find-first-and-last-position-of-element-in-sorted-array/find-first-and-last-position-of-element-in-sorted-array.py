class Solution(object):
    def searchRange(self, nums, target):
        def findFirst(nums, target):
            low, high = 0, len(nums) - 1
            first = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
                if nums[mid] == target:
                    first = mid
            return first

        def findLast(nums, target):
            low, high = 0, len(nums) - 1
            last = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
                if nums[mid] == target:
                    last = mid
            return last

        return [findFirst(nums, target), findLast(nums, target)]

        