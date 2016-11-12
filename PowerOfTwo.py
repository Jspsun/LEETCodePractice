class Solution(object):

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n == 2:
            return True
        number = 2
        while (number <= n):
            number *= 2
            if(number == n):
                return True
        return False
