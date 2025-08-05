class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = []          # to store current substring with no duplicates
        max_len = 0        # to keep track of max length

        for ch in s:
            if ch in seen:
                while ch in seen:
                    seen.pop(0)   # remove from the start until duplicate is gone
            seen.append(ch)       # add current character
            if len(seen) > max_len:
                max_len = len(seen)  # update max length if current is longer

        return max_len

