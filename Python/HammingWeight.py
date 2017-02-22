class Solution(object):

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

s = Solution()
print s.hammingWeight(11)
