from typing import List

# Recursive helper function
def f(arr, idx, subset, ans, k):
    # If current subset is too long, stop
    if len(subset) > k:
        return

    # If we've considered all elements
    if idx == len(arr):
        if len(subset) == k:
            ans.append(subset)
        return

    # Include current element
    f(arr, idx + 1, subset + [arr[idx]], ans, k)

    # Exclude current element
    f(arr, idx + 1, subset, ans, k)


# Main solution class
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []
        for i in range(n):
            arr.append(i + 1)

        ans = []
        f(arr, 0, [], ans, k)
        return ans
