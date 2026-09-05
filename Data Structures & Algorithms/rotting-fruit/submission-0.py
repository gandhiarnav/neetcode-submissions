class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] ==2:
                    q.append((i,j))
        print(fresh)
        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)   
        ]
        step_count = 0
        flag = False
        print(q)
        while q:
            step_count += 1
            flag = False
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
                        if grid[nr][nc] == 1:
                            flag = True
                            fresh-=1
                            grid[nr][nc] = 2
                            q.append((nr,nc))
            print(q)
            if flag:
                continue
            else:
                step_count-=1
        print(fresh)
        if fresh:
            return -1
        return step_count



            