class Solution(object):
    def flipAndInvertImage(self, A):
        for row in A:
            for i in xrange((len(row) + 1) / 2):
                # ~ operator (not operator) x*-1-1 <- gets the element on the oposite side
                row[i], row[~i] = ~row[~i] ^ 1, row[i] ^ 1
        return A
