class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        lpletter=[ ch.lower() for ch in licensePlate if ch.isalpha()]
        lpcount=Counter(lpletter)

        result=None

        for word in words:
            wordcount = Counter(word.lower())

            if all(wordcount[char]>= lpcount[char] for char in lpcount):
                if result is None or len(word)<len(result):
                    result = word
        return result
        