import math


class Solution(object):

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # t = 0
        # r = 1
        # while True:
        #     n -= r
        #     r += 1
        #     if n >= 0:
        #         t += 1
        #     else:
        #         break
        # return t

        # or use sum of series
        return int((math.sqrt(1 + 8.0 * n) - 1) / 2)

print Solution().arrangeCoins(8)
