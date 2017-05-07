class Solution(object):

    def checkRecord(self, n):
        if n == 1:
            return 3
        if n == 0:
            return 0
        nums = [1, 1, 2]
        i = 2
        while i < n:
            nums.append((nums[i] + nums[i - 1] + nums[i - 2]) % 1000000007)
            i += 1
        result = (nums[n] + nums[n - 1] + nums[n - 2]) % 1000000007
        for i in range(n):
            result += nums[i + 1] * nums[n - i] % 1000000007
            result %= 1000000007
        return result

    # permutations method
    # total = 0
    #
    # def checkRecord(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     self.permute([], n)
    #     return self.total % (10**9 + 7)
    #
    # # permute all valid cases
    # def permute(self, s, n):
    #     if len(s) == n:
    #         # print s
    #         self.total += 1
    #         return
    #     if len(s) < 2 or (s[-1] != 'L' or s[-2] != 'L'):
    #         self.permute(s[:] + ['L'], n)
    #     if 'A' not in s:
    #         self.permute(s[:] + ['A'], n)
    #     self.permute(s[:] + ['P'], n)

print Solution().checkRecord(14)
