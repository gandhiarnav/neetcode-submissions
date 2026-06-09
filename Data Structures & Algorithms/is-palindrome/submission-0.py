import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sn = s.lower()
        sn = re.sub(r'[^0-9a-z]','',sn)
        print(sn)
        f=0
        b=len(sn)-1
        while f<=b:
            if sn[f] != sn[b]:
                return False
            else:
                f+=1
                b-=1
        return True


        