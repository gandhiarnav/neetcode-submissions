class Solution:
    def isHappy(self, n: int) -> bool:
        newn = 0
        seen = set()
        while n != 1:
            while n:
                newn += (n%10)**2
                n = n // 10
                
            # print(n, newn)
            if newn in seen:
                return False
            seen.add(newn)
            n= newn
            newn = 0
        return True

        # print(newn)