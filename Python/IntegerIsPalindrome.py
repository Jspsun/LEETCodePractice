class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if (x < 0 or (x != 0 and x % 10 == 0)):
            return False

        temp = x
        newN = 0
        while x > newN:
            newN = newN * 10 + temp % 10
            temp /= 10
        return newN == x or newN / 10 == x

print Solution().isPalindrome(10)
