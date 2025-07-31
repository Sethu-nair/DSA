class Solution(object):
    def isAnagram(self, s, t):
        def getDictionary(string):
            d = {}
            for char in string:
                if char in d:
                    d[char] += 1
                else:
                    d[char] = 1
            return d

        return getDictionary(s) == getDictionary(t)
