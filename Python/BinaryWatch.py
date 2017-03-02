class Solution(object):

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        list = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count("1") == num:
                    list.append('%d:%02d' % (h, m))
        return list

S = Solution()
print S.readBinaryWatch(1)
