class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ll=0
        l=0
        done=set()
        for r in range(0,len(s)):
            while s[r] in done:
                done.remove(s[l])
                l+=1
            done.add(s[r])
            ll=max(ll,r-l+1)

        return ll
