class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""
        
        occ_t = {}
        occ_s = {}

        for c in t:
            occ_t[c] = 1 + occ_t.get(c,0)
        
        need = len(occ_t)

        have = 0

        res = [-1,-1]
        res_len = float("inf")

        l=0

        for r in range(len(s)):
            c=s[r]
            occ_s[c] = 1 + occ_s.get(c,0)

            if c in occ_t and occ_s[c] == occ_t[c]:
                have += 1

            #trying to shrink the string
            while have == need:
                if (r-l+1) < res_len:
                    res = [l,r]
                    res_len = r-l+1
                #pop from left:
                left_c = s[l]
                occ_s[left_c] -= 1
                
                if left_c in occ_t and occ_s[left_c] < occ_t[left_c]:
                    have -=1

                l+=1

        l,r = res
        return s[l:r+1] if res_len != float("inf") else ""
        

        


            


        
            

        