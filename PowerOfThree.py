class Solution(object):

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n % 1 != 0 or n < 3:
            return False
        else:
            return self.isPowerOfThree(n / 3.0)
