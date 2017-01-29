class Solution(object):

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsTotal = 0
        for n in nums:
            numsTotal += n

        n = len(nums)
        trueTotal = (n * (n + 1)) / 2
        return trueTotal - numsTotal

s = Solution()
print s.missingNumber([])
