class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        //"""
        
        n = len(startTime)

        # 1. Construct the array of initial gap durations.
        # There are n meetings, leading to n+1 potential gaps.
        gaps = []
        
        # Gap before the first meeting: from time 0 to startTime[0]
        gaps.append(startTime[0])
        
        # Gaps between consecutive meetings: from endTime[i] to startTime[i+1]
        for i in range(n - 1):
            gap = startTime[i+1] - endTime[i]
            gaps.append(gap)
            
        # Gap after the last meeting: from endTime[n-1] to eventTime
        gaps.append(eventTime - endTime[n-1])

        # With `k` reschedules, we can merge a block of `k+1` contiguous gaps.
        # The problem becomes finding the maximum sum of a contiguous subarray of gaps.
        # Since all gap durations are non-negative, we want the longest possible subarray,
        # which has size m = k+1 (or the total number of gaps if smaller).

        # 2. Determine the window size for the sliding window.
        num_gaps = n + 1
        m = min(k + 1, num_gaps)

        # 3. Use a sliding window of size m to find the maximum sum.
        
        # Calculate the sum for the first window of size m
        current_sum = sum(gaps[0:m])
        max_sum = current_sum

        # Slide the window across the rest of the array to find the max sum
        for i in range(m, num_gaps):
            # Update the window sum by adding the new element and removing the old one
            current_sum += gaps[i] - gaps[i - m]
            if current_sum > max_sum:
                max_sum = current_sum
            
        return max_sum