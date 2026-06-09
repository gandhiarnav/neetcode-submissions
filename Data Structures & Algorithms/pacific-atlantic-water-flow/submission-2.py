class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows,cols = len(heights),len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(r,c,visit,pervHeight):
            if ((r,c) in visit or
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                heights[r][c] < pervHeight 
            ):
                return      

            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])


        for c in range(cols):
            dfs(0,c,pacific,heights[0][c])
            dfs(rows-1,c,atlantic,heights[rows-1][c])
        for r in range(rows):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,cols-1,atlantic,heights[r][cols-1])

        both = pacific & atlantic
        print(pacific)
        print(atlantic)
        print(both)
        for (x,y) in both:
            res.append([x,y])
        return res    
                
