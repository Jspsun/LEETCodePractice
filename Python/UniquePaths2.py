class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        width =  len(obstacleGrid[0])
        memo =  [0]*width
        memo[0]=1
        for r in obstacleGrid:
            for c in xrange(len(r)):
                if r[c] == 1:
                    memo[c]=0
                elif c!= 0:
                    memo[c]=memo[c]+memo[c-1]
        return memo[width-1]



print Solution().uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])
