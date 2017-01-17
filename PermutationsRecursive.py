class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutation = []
        self.helper([], nums, permutation)
        return permutation

    def helper(self, array, remaining, permutation):
        if len(remaining) == 0:
            permutation.append(array)
            return
        for i in range(len(remaining)):
            self.helper(array + [remaining[i]], remaining[:i] +
                        remaining[i + 1:], permutation)

s = Solution()
print s.permute([1, 2, 3])
