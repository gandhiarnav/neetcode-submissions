class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        Rows ,Cols = len(board), len(board[0])
        lenWord = len(word)
        def dfs(r,c,i):
            if i == lenWord:
                return True
            if r >= Rows or c >= Cols or min(r,c) < 0 or word[i] != board[r][c] or (r,c) in path:
                return  False

            path.add((r,c))
            res = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            path.remove((r,c))
            return res

        for i in range(0,Rows):
            for j in range(0, Cols):
                if dfs(i,j,0):
                    return True
        return False
                
