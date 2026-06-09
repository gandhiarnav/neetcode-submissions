class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        l = len(s)-1

        while i <= l:
            
            s[i],s[l] = s[l],s[i]
            i+=1
            l-=1
        
        