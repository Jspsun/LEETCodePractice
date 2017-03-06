# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Binary Search
        l = 0
        r = n
        while l <= r:
            m = (l + r) / 2
            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        return l
