class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        h = defaultdict(list)

        h = {i:[] for i in range(numCourses)}

        for i,j in prerequisites:
            if i in h:
                h[i].append(j)

        print(h)

        visiting = set()

        def dfs(n):
            if n in visiting:
                return False
            if h[n] == []:
                return True
            
            visiting.add(n)

            for p in h[n]:
                if not dfs(p):
                    return False
            visiting.remove(n)
            h[n] = []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


                