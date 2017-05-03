class Solution(object):

    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        nlist = [[None for col in range(c)] for row in range(r)]
        for oR in nums:
            for oC in nums:


print Solution().matrixReshape([1, 2, 3], 5, 2)
