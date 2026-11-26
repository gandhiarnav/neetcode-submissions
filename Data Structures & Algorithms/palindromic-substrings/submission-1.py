class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        n = len(s)

        for i in range(n):

            #odd pals
            l,r = i,i
            while l>=0 and r<n and s[l] == s[r]:
                c+=1
                l-=1
                r+=1
            
            #even pals
            l,r = i-1,i
            while l>=0 and r<n and s[l] == s[r]:
                c+=1
                l-=1
                r+=1

        return c