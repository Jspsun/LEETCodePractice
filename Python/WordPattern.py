class Solution(object):

    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        # gets the index of each char within the string and generates a list
        sDex = map(s.find, s)
        # gets the index of each word within the array and generates a list
        tDex = map(t.index, t)
        return sDex == tDex

S = Solution()
print S.wordPattern("abba", "a b b a")
