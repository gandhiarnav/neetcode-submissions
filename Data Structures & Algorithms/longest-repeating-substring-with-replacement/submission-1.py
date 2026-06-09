class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        max_l = 1
        win_l = 1
        cnt = {}
        res = 1
        while r<len(s):
            win_l = r-l+1
            if s[r] in cnt:
                cnt[s[r]] += 1
            else:
                cnt[s[r]] = 1
            max_l = max(max_l, cnt[s[r]])
            if win_l - max_l <=k:
                res = max(res, win_l)
            else:
                cnt[s[l]] -= 1
                l+=1
            r+=1
        return res 
