class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxEndingHere = nums[0]
        maxSoFar = nums[0]

        for i in range(1, len(nums)):
            maxEndingHere = max(nums[i], maxEndingHere + nums[i])
            maxSoFar = max(maxEndingHere, maxSoFar)

        return maxSoFar
