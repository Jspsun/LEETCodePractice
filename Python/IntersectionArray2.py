class Solution(object):

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        for n in nums2:
            if n not in dict:
                dict[n] = 1
            else:
                dict[n] += 1
        ret = []
        for n in nums1:
            if n in dict and dict[n] > 0:
                ret.append(n)
                dict[n] -= 1
        return ret
