class Solution(object):

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list = set()
        result = []
        for n in nums:
            if n in list:
                result.append(n)
            else:
                list.add(n)
        return result
