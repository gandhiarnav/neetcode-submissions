class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        if not temperatures:
            return res
        for i in range(0,len(temperatures)):
            itr = 0
            for j in range(i+1,len(temperatures)):
                itr+=1
                if temperatures[i]<temperatures[j]:
                    res.append(itr)
                    break
                if itr>=(len(temperatures)-i-1):
                    res.append(0)

        res.append(0)
        return res

