class Solution(object):

    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # could use this too
        # print int(''.join(int(math.floor(math.log(num, 2) + 1)) * ['1']), 2)
        i = 1
        while i <= num:
            i = i << 1

        return num ^ (i - 1)

print Solution().findComplement(2)
