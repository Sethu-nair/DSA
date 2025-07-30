class Solution(object):
    def maxProfit(self, prices):
        minprice=float('inf')
        maxprofit=0
        for i in prices:
            if i<minprice:
                minprice=i
            else:
                maxprofit=max(maxprofit,i-minprice)
        return maxprofit


        