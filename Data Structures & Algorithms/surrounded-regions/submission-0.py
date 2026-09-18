class Solution:
    def solve(self, board: list[list[str]]) -> None:
        ROW,COL = len(board), len(board[0])
        
        def dfs(i,j):
            if i < 0 or j < 0 or i == ROW or j == COL or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)


        for i in range(ROW):
            for j in range(COL):
                if i == 0 or j == 0 or i == ROW-1 or j == COL-1:
                    if board[i][j] == 'O':
                        dfs(i,j)

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == 'T':
                    board[i][j] = 'O'

        
