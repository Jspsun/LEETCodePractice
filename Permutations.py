class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in xrange(len(perm) + 1):
                    new_perms.append(perm[:i] + [n] + perm[i:])  # insert n
            perms = new_perms
        return perms


s = Solution()
print s.permute([1, 1, 2])
