class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Case 1 & 2: Subsequences of all same-parity numbers.
        # The length is simply the total count of even or odd numbers in the array.
        count_even = 0
        count_odd = 0
        for num in nums:
            if num % 2 == 0:
                count_even += 1
            else:
                count_odd += 1

        # Case 3: Alternating parity subsequence starting with an even number.
        len_alt_start_even = 0
        expected_parity_1 = 0  # Start expecting an even number (0)
        for num in nums:
            if num % 2 == expected_parity_1:
                len_alt_start_even += 1
                # Flip the expectation for the next number in the subsequence
                expected_parity_1 = 1 - expected_parity_1

    # Case 4: Alternating parity subsequence starting with an odd number.
        len_alt_start_odd = 0
        expected_parity_2 = 1  # Start expecting an odd number (1)
        for num in nums:
            if num % 2 == expected_parity_2:
                len_alt_start_odd += 1
                # Flip the expectation for the next number in the subsequence
                expected_parity_2 = 1 - expected_parity_2
        
        # The final answer is the maximum length found among all four possibilities.
        return max(count_even, count_odd, len_alt_start_even, len_alt_start_odd)