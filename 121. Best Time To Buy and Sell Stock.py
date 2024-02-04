class Solution(object):
    def maxProfit(self, prices):
        """ 
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        maxprofit=0
        localmin=prices[0]
        for i in range(1, n):
            if prices[i] > localmin:
                profit=prices[i]-localmin
                maxprofit=max(maxprofit, profit)
            else:
                localmin=prices[i]
        return maxprofit
