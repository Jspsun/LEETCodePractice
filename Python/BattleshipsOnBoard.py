class Solution(object):

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        # cycle through each point
        # check surrounding
        # add one
        # set surroundgs to .

        count = 0
        for row in range(0, len(board)):
            for column in range(0, len(board[0])):
                if board[row][column] == 'X':
                    if (row == 0 or board[row - 1][column] != 'X')and(column == 0 or board[row][column - 1] != 'X'):
                        count += 1
        return count
