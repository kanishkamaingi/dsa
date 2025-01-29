class Solution(object):
    def isValidSudoku(self, board):
        from collections import defaultdict
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows_dict = defaultdict(set)
        cols_dict = defaultdict(set)
        sq_dict = defaultdict(set)

        for r in range(0, 9):
            for c in range(0,9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows_dict[r]) or (board[r][c] in cols_dict[c]) or (board[r][c] in sq_dict[(r//3, c//3)]):
                    return False

                cols_dict[c].add(board[r][c])
                rows_dict[r].add(board[r][c])
                sq_dict[(r//3, c//3)].add(board[r][c])

        return True




        