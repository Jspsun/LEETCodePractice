class Solution(object):

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # count numbers before 0s
        leadingN = 0
        for i in range(len(num)):
            if num[i] != "0":
                leadingN += 1
            else:
                break
        if leadingN <= k:
            k -= leadingN
            num = num[leadingN + 1:]

        # find k highest numbers
        # this is a huge bottleneck need to fix
        for i in range(k):
            highi = 0
            for j in range(len(num)):
                if int(num[:j] + num[j + 1:]) < int(num[:highi] + num[highi + 1:]):
                    highi = j
            num = num[:highi] + num[highi + 1:]
        num = "0" + num[:]
        return str(int(num))

s = Solution()
print s.removeKdigits("10", 2)
