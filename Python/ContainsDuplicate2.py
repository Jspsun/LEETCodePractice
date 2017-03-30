class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # k = abs(k)
        m = {}
        for i in range(len(nums)):
            if nums[i] in m:
                if i - m[nums[i]] <= k:
                    return True
                else:
                    m[nums[i]] = i
            else:
                m[nums[i]] = i
        return False

S = Solution()
print S.containsNearbyDuplicate([1, 2, 1], 1)
