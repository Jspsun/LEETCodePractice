class Solution(object):

    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = [0 for i in range(11)]
        for i in range(len(s)):
            c = s[i]
            if (c == 'z'):
                count[0] += 1
            if (c == 'w'):
                count[2] += 1
            if (c == 'x'):
                count[6] += 1
            if (c == 's'):
                count[7] += 1
            if (c == 'g'):
                count[8] += 1
            if (c == 'u'):
                count[4] += 1
            if (c == 'f'):
                count[5] += 1
            if (c == 'h'):
                count[3] += 1
            if (c == 'i'):
                count[9] += 1
            if (c == 'o'):
                count[1] += 1

        count[7] -= count[6]
        count[5] -= count[4]
        count[3] -= count[8]
        count[9] = count[9] - count[8] - count[5] - count[6]
        count[1] = count[1] - count[0] - count[2] - count[4]
        r = ""
        for i in range(10):
            for j in range(count[i]):
                r += str(i)

        return r
