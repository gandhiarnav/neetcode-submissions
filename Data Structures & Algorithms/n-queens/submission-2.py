class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        cols = set()
        pos_diag = set()  # r + c
        neg_diag = set()  # r - c

        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return

            for c in range(n):
                # O(1) conflict check
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # Place queen and record lines
                board[r][c] = 'Q'
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                backtrack(r + 1)

                # Backtrack / cleanup
                board[r][c] = '.'
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        backtrack(0)
        return res