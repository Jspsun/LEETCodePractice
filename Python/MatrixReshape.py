class Solution(object):

    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        nlist = [[None for col in range(c)] for row in range(r)]
        if c * r != len(nums) * len(nums[0]):
            return nums
        counter = 0
        for oR in nums:
            for oC in oR:
                if counter / c > r:
                    return nums
                nlist[counter / (c)][counter % c] = oC
                counter += 1
        return nlist

print Solution().matrixReshape([[1, 2, 3], [4, 5, 6]], 5, 2)
