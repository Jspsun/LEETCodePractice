import string


class Solution(object):

    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        sign = 1
        # get sign
        if num < 0:
            sign = -1
        elif num == 0:
            return '0'

        num *= sign

        list = []
        while num > 0:
            list.append(str(num % 7))
            num /= 7
        if sign == -1:
            list.append('-')
        list.reverse()
        return ''.join(list)

S = Solution()
print S.convertToBase7(0)
