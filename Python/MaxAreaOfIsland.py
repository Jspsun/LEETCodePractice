class Solution(object):
    max = 0
    count = 0
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.max=0
        for r in xrange(len(grid)):
            for c in xrange(len(grid[0])):
                self.count = 0
                self.explore(r,c,grid)
        return self.max

    
    def explore(self, r, c, grid):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c]==0:
            return
        self.count += 1
        grid [r][c] = 0
        self.max = max(self.count, self.max)
        self.explore(r-1,c,grid)
        self.explore(r+1,c,grid)
        self.explore(r,c-1,grid)
        self.explore(r,c+1,grid)

print Solution().maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])