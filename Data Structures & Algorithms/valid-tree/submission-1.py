class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nbs = defaultdict(list)
        for j,k in edges:
            nbs[j].append(k)
            nbs[k].append(j)
        # print(nbs)
        visited = set()

        def dfs(node,parent):
            for i in nbs[node]:
                if i == parent:
                    continue
                if i in visited:
                    return False
                visited.add(i)
                if not dfs(i,node):
                    return False
            return True
            

        visited = set()
        visited.add(0)
        if not dfs(0,-1):
            return False
        # print(visited)
    
        if len(visited) != n:
            return False

        return True


