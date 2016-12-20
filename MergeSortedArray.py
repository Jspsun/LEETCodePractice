class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i1 = 0
        i2 = 0
        total = m + n
        while i1 < m and i2 < n:
            if nums2[i2] < nums1[i1]:
                self.shift(nums1, i1, total)
                nums1[i1] = nums2[i2]
                i1 += 1
                i2 += 1
                m += 1
            else:
                i1 += 1
        if(i2 < n):
            while(i2 < n):
                nums1[i1] = nums2[i2]
                i1 += 1
                i2 += 1

    def shift(self, nums, index, length):
        length -= 1
        while(length > index):
            nums[length] = nums[length - 1]
            length -= 1

s = Solution()

# ListOne = [1, 3, 5, 6, 0, 0, 0, 0]
# lOne = 4
# ListTwo = [2, 4, 7, 8]
# lTwo = 4


ListOne = [0]
lOne = 0
ListTwo = [1]
lTwo = 1



s.merge(ListOne, lOne, ListTwo, lTwo)

print ListOne
