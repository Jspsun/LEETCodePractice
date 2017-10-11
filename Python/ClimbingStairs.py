class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [1,2]
        for i in range (2, n):
            memo.append(memo[i-1] + memo [i-2])
        return memo[n-1]
