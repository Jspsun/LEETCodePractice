import string

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        l = list(string.ascii_uppercase)
        s = []
        while(n > 0):
            s.append(l[(n-1) % 26])
            n = (n - 1)//26
        s.reverse()
        return ''.join(s)
