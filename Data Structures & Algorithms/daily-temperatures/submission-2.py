class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for x in temperatures]
        print(res)
        stk = []
        for i, ele in enumerate(temperatures):
            while stk and ele > stk[-1][1]:
                si, sele = stk.pop()
                res[si] = i - si
            stk.append((i,ele))
        return res
                
            