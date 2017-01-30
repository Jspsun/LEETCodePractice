class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 0:
            return 0

        lowest = prices[0]
        profit = 0
        for cost in prices:
            if cost < lowest:
                lowest = cost
            temp = cost - lowest
            if temp > profit:
                profit = temp
        return profit

s = Solution()
print s.maxProfit([])
