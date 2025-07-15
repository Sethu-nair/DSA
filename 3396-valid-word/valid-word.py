class Solution(object):
    def isValid(self, word):
        if(len(word)<3):
            return False

        vowels=set('aeiouAEIOU')
        hasvowel=False
        hasconstant=False

        for ch in word:
            if not ch.isalnum():
                return False
            if ch.isalpha():
                if ch in vowels:
                    hasvowel=True
                else:
                    hasconstant=True
        return hasvowel and hasconstant

        