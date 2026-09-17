class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = set()
        q = deque()
        ROW,COL = len(grid), len(grid[0])
        INF = 2147483647
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))

        def addQue(r,c):
            if r < 0 or c < 0 or r == ROW or c == COL or grid[r][c] == -1 or (r,c) in visit:
                return
            # print(f"appending({r},{c})")
            q.append((r,c))
            visit.add((r,c))


        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                # visit.add(grid[r][c])
                # print(dist)
                addQue(r+1,c)
                addQue(r-1,c)
                addQue(r,c+1)
                addQue(r,c-1)
            dist+=1



