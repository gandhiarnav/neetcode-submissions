class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        noIsland = 0
        curmaxArea = 0
        def dfs(r,c):
            nonlocal curmaxArea
            if r<0 or c<0 or r>= len(grid) or c>= len(grid[r]) or grid[r][c] == 0:
                return
            
            curmaxArea+=1
            grid[r][c] = 0
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    curmaxArea = 0
                    dfs(i,j)
                maxArea = max(curmaxArea,maxArea)
        return maxArea


            