class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        def generateRow(rowsToGen, above, list):
            if rowsToGen <= 0:
                return
            list.append(above)
            temp = [1]
            for i in range(0, len(list) - 1):
                temp.append(above[i] + above[i + 1])
            temp.append(1)
            generateRow(rowsToGen - 1, temp, list)

        l = []
        generateRow(numRows, [1], l)
        return l

print Solution().generate(5)
