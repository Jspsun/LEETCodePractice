class Solution(object):
    def minCostClimbingStairs(self, cost):
        l = len(cost)
        dp = [float("inf") for i in range(l)]
        dp[0]=0
        dp[1]=0
        for i in xrange(2, l):
            dp[i]=min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return min (dp[l-2], dp[l-3])



print Solution().minCostClimbingStairs([0,0,0,1])
