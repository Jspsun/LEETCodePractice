class Solution(object):

    def removeKdigits(self, num, k):
        out = []
        for n in num:
            while len(out) > 0 and k > 0 and out[-1] > n:
                out.pop()
                k -= 1
            out.append(n)

        return ''.join(out[:-k or None]).lstrip('0') or "0"

s = Solution()
print s.removeKdigits("9", 1)
