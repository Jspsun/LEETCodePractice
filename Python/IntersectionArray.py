class Solution(object):

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s = set(nums2)
        vals = []
        for n in nums1:
            if n in s:
                vals.append(n)
                s.remove(n)
        return vals
