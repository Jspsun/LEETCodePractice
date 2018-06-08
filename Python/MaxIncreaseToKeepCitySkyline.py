class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum=0
        side=[]
        top=[0 for i in range(len(grid[0]))]
        for r in range(len(grid)):
            #get side skyline
            side.append(max(grid[r]))
            for c in range(len(grid[r])):
                top[c]= max([top[c], grid[r][c]])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # grid[r][c]=min([side[r],top[c]])
                sum+=min([side[r],top[c]])-grid[r][c]
        return sum



print Solution().maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])

