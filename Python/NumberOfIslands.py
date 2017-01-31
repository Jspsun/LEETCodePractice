class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.clearIsland(grid, r, c)
                    count += 1
        return count

    def clearIsland(self, grid, r, c):
        grid[r][c] = "0"
        if r > 0 and grid[r - 1][c] == "1":
            self.clearIsland(grid, r - 1, c)
        if r < len(grid) - 1 and grid[r + 1][c] == "1":
            self.clearIsland(grid, r + 1, c)
        if c > 0 and grid[r][c - 1] == "1":
            self.clearIsland(grid, r, c - 1)
        if c < len(grid[0]) - 1 and grid[r][c + 1] == "1":
            self.clearIsland(grid, r, c + 1)
        return
