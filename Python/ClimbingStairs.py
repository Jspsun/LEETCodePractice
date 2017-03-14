class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0, 1, 2]
        for n in range(3, n + 1):
            memo.append(memo[n - 2] + memo[n - 1])
        return memo[n]

S = Solution()
print S.climbStairs(4)
