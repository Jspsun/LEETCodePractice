class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        r = []

        def generateRow(rowsToGen, above):
            if rowsToGen < 0:
                return
            self.r = above
            temp = [1]
            for i in range(0, len(above) - 1):
                temp.append(above[i] + above[i + 1])
            temp.append(1)
            generateRow(rowsToGen - 1, temp)

        generateRow(rowIndex, [1])
        return r

print Solution().getRow(2)
