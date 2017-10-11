class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxSum = nums[0]
        currentSum = nums[0]
        for n in nums[1:]:
            currentSum = max(n, currentSum + n)
            maxSum = max(maxSum, currentSum)
        return maxSum