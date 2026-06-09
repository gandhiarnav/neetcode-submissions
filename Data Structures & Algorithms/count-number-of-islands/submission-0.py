class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.res = 0
        seen = set()
        Len = len(grid)
        Wid = len(grid[0])

        def dfs(l,w):
            if l<0 or w<0 or l>=Len or w>=Wid or grid[l][w] == "0" or (l,w) in seen:
                return
            if grid[l][w] == "1":
                lst = [(l-1,w),(l+1,w),(l,w-1),(l,w+1)]
                if not set(lst) & seen:
                    self.res+=1
                seen.add((l,w))
                dfs(l-1,w)
                dfs(l+1,w)
                dfs(l,w-1)
                dfs(l,w+1)

        for i in range(Len):
            for j in range(Wid):
                dfs(i,j)
        print(seen)
        return self.res


        