class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        permutations = []

        # manual case for blank array
        if digits == "":
            return []

        map = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': [
            'm', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        self.helper("", digits, permutations, map)
        return permutations

    def helper(self, array, remaining, permutations, map):
        if len(remaining) == 0:
            permutations.append(array)
            return
        for letter in map[remaining[0]]:
            self.helper(array + letter, remaining[1:], permutations, map)

s = Solution()
print s.letterCombinations("23")
