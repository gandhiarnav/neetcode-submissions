class Solution:
    def isPal(self,s,i,j):
        s = s[i:j+1]
        if s != s[::-1]:
                return False
        return True


    def partition(self, s: str) -> List[List[str]]:
        res = []
        pals = []

        def dfs(i):
            if i >= len(s):
                res.append(pals.copy())
                return
            for j in range(i,len(s)):
                if self.isPal(s,i,j):
                    pals.append(s[i:j+1])
                    dfs(j+1)
                    pals.pop()
        dfs(0)
        return res

