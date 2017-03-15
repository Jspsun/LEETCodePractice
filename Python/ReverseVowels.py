class Solution(object):

    # could do with two pointers on either end and then swap vowels
    # both are o(n) but two pointers is one pass
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        toSwitch = []
        for l in s:
            if l in vowels:
                toSwitch.append(l)
        toSwitch.reverse()
        switchDex = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = toSwitch[switchDex]
                switchDex += 1
        return ''.join(s)


S = Solution()
print S.reverseVowels("eqadasdfadhjkjjkappwad")
