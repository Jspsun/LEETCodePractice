class Solution(object):

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list = set(nums)
        result = []
        for i in range(1, len(nums) + 1):
            if i not in list:
                result.append(i)
        return result
