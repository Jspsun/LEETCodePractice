class Solution(object):

    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # get length of the number we need
        # get the actaul number
        # return the nth digit
        length = 1
        number = 1
        counter = 9
        while n > length * counter:
            n -= length * counter
            length += 1
            counter *= 10
            number *= 10
        number += (n - 1) / length
        number = str(number)
        return int(number[(n - 1) % length])

S = Solution()
print S.findNthDigit(11)
