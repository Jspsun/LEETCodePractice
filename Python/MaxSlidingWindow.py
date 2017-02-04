from collections import deque


class Solution(object):

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        q = deque()
        r = []
        for i in range(len(nums)):
            # remove numbers not in range k
            while q and (q[0] < i - k + 1):
                q.popleft()
            # remove numbers smaller than nums[i]
            while q and (nums[q[-1]] < nums[i]):
                q.pop()
            # appaends the head of the q which is the max element in
            # [i-(k-1),i]
            q.append(i)
            if i >= k - 1:
                r.append(nums[q[0]])
        return r
