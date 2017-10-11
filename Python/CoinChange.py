class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 1:
            return 0
        count = [0 for i in xrange(amount + 1)]
        self.helper(coins, amount, count)
        return count[amount]
    
    def helper(self, coins, remainder, count):
        if remainder <0:
            return -1
        if remainder == 0:
            return 0
        if count[remainder]!=0:
            return count[remainder]
        min = 9999999
        for c in coins:
            noOfCoinsNeeded = self.helper(coins, remainder - c, count)
            if noOfCoinsNeeded >=0 and noOfCoinsNeeded < min:
                min = 1 + noOfCoinsNeeded
        if min != 9999999:
            count [remainder] = min
        else:
            count [remainder] = -1
        return count[remainder]