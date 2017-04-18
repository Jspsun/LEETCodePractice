class Solution:
    # @param n, an integer
    # @return an integer

    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], 2)

S = Solution()
print S.reverseBits(43261596)
