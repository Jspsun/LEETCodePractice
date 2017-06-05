
# DFS NO LONGER WORKS BECAUSE OF TLE

#
# class Solution(object):
#     total = 0
#
#     def findTargetSumWays(self, nums, S):
#         """
#         :type nums: List[int]
#         :type S: int
#         :rtype: int
#         """
#         self.total = 0
#         n = len(nums)
#         sums = range(n)
#         sums[n - 1] = nums[n - 1]
#         for i in range(len(nums) - 2, -1, -1):
#             sums[i] = sums[i + 1] + nums[i]
#         self.dfs(nums, sums, S, 0)
#         return self.total
#
#     def dfs(self, nums, sums, S, position):
#         if position == len(nums):
#             if S == 0:
#                 self.total += 1
#             return
#
#         if (sums[position] < abs(S)):
#             return
#
#         self.dfs(nums, sums, S + nums[position], position + 1,)
#         self.dfs(nums, sums, S - nums[position], position + 1,)
#
# print Solution().findTargetSumWays([1, 1, 1, 1, 1], 3)


class Solution(object):

    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)
