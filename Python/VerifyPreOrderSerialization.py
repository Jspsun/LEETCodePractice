class Solution(object):

    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(",")
        s = []

        for n in nodes:
            s.append(n)
            while (self.endsWithTwoHashes(s)):
                s.pop()
                s.pop()
                if len(s) <= 0:
                    return False
                s.pop()
                s.append('#')
        if len(s) == 1:
            if s[0] == '#':
                return True
        return False

    def endsWithTwoHashes(self, stack):
        if len(stack) >= 2:
            if stack[-1] == '#' and stack[-2] == '#':
                return True
        return False

s = Solution()
s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
