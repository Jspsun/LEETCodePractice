class Solution(object):

    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # sketchy but works
        greaterThanZero = (num > 0)
        powerOfTwo = ((num & (num - 1)) == 0)
        oneInOddPosition = ((num & 0x55555555) == num)
        return greaterThanZero and powerOfTwo and oneInOddPosition
