class Solution(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # at the same time load into set
        list = set(nums)
        min = 0
        while(True):
            if min + 1 not in list:
                return min + 1
            min += 1

s = Solution()
print s.firstMissingPositive([3, 4, -1, 1])
