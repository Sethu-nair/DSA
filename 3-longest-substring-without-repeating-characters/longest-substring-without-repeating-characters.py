class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = []    
        max_len = 0      

        for ch in s:
            if ch in seen:
                while ch in seen:
                    seen.pop(0)  
            seen.append(ch)      
            if len(seen) > max_len:
                max_len = len(seen)

        return max_len

        