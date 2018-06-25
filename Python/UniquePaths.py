class Solution(object):
    # def uniquePaths(self, m, n):
    #     """
    #     :type m: int
    #     :type n: int
    #     :rtype: int
    #     """
    #     memo =[[1]*m for i in xrange(n)]
    #     memo[0][0]=1
    #     for r in xrange(1, n):
    #         for c in xrange(1,m):
    #             memo[r][c] = memo[r-1][c] + memo[r][c-1]
    #     return memo[n-1][m-1]
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = [1]*m
        for r in xrange(1, n):
            for c in xrange(1,m):
                memo[c] = memo[c] + memo[c-1]
        return memo[m-1]

print Solution().uniquePaths(7, 3)
