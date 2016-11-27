class Solution(object):

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # cycle through each element and count the perimeter
        # Perimeter of each block with land is 4-occupied sides

        total = 0

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    surrounding = 0
                    # cases for each edge
                    # check above
                    if row != 0:
                        if grid[row - 1][column] == 1:
                            surrounding += 1
                    # check below
                    if row != len(grid) - 1:
                        if grid[row + 1][column] == 1:
                            surrounding += 1
                    # check left
                    if column != 0:
                        if grid[row][column - 1] == 1:
                            surrounding += 1
                    # check right
                    if column != len(grid[0]) - 1:
                        if grid[row][column + 1] == 1:
                            surrounding += 1
                    total += 4 - surrounding
        return total
