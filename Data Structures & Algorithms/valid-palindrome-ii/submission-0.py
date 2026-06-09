class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^1-9a-z]','',s)

        i = 0
        l = len(s)-1
        res = set()
        flag = True
        while i <= l:
            if s[i] != s[l]:
                res.add(False)
                flag = False
                break
            i+=1
            l-=1
        if flag:
            res.add(True)

        for i in range(len(s)):
            ns=""
            for j in range(len(s)):
                if i != j:
                    ns = ns + s[j]
            print(ns)
            r = 0
            l = len(ns)-1
            flag = True
            while r <= l:
                if ns[r] != ns[l]:
                    res.add(False)
                    print(res)
                    flag = False
                    break
                r+=1
                l-=1
            if flag:
                res.add(True)
                print(res)

        if True in res:
            return True
        else:
            return False