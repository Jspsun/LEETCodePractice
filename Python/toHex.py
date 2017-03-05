class Solution(object):

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # dex = {'0', '1', '2', '3', '4', '5', '6', '7',
        #        '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}

        dex = '0123456789abcdef'
        if num == 0:
            return '0'
        res = ''
        while(num != 0 and len(res) < 8):
            res = dex[num & 15] + res
            num = num >> 4
        return res

S = Solution()
print S.toHex(-1)
