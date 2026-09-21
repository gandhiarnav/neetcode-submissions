class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        h = defaultdict(list)

        for i in range(numCourses):
            h[i] = []
        
        for i,j in prerequisites:
            h[i].append(j)
        res = []
        visiting = set()
        visited = set()
        def dfs(n):
            if n in visiting:
                return False
            if h[n] == []:
                if n not in visited:
                    res.append(n)                                   
                    visited.add(n)
                return True
            visiting.add(n)
            for preq in h[n]:
                if not dfs(preq):
                    return False    

            visiting.remove(n)

            h[n] = []
            if n not in visited:
                res.append(n)                                   
                visited.add(n)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []

        print(visited)
        return res
