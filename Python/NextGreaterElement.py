class Solution(object):

    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        s = []
        m = {}
        for n in nums:
            while len(s) > 0 and s[-1] < n:
                m[s.pop()] = n
            s.append(n)

        return [m.get(n, -1) for n in findNums]


print Solution().nextGreaterElement([1, 0], [1, 0, 2, 3])
