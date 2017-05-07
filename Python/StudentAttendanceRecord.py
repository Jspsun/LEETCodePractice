class Solution(object):

    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        noAbs = 0
        contL = 0

        for l in s:
            if l == 'A':
                noAbs += 1
                contL = 0
            elif l == 'L':
                contL += 1
            else:
                contL = 0
            if noAbs > 1 or contL > 2:
                return False
        return True
