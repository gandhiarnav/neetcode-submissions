class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n== 0:
            return 1
        if n == 1:
            return x
        if x == 1:
            return 1
        if x == 0:
            return 0

        if x == -1:
            if n%2 == 0:
                return 1
            else:
                return -1

        if n<-200000:
            return 0

        if n>1:
            res = x
            mul = x
        else:
            res = 1/x
            mul = 1/x
            n = n*-1

        for i in range(n-1):
            # print(i,res)
            res *= mul
        return res