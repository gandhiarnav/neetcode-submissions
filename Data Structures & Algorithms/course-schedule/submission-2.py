class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        h = defaultdict(list)

        for i in range(numCourses):
            h[i] = []
        
        for i,j in prerequisites:
            h[i].append(j)
        
        visiting = set()

        def dfs(n):
            if n in visiting:
                return False
            if h[n] == []:
                return True
            visiting.add(n)
            for preq in h[n]:
                if not dfs(preq):
                    return False
            visiting.remove(n)
            h[n] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


