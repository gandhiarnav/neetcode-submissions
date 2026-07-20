import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        o_need = dict([(x,0) for x in s1])
        for i in s1:
            o_need[i] +=1
        need = copy.deepcopy(o_need)
        print(need)

        l=0
        r=0
        while l<len(s2):
            
            if s2[l] in need:
                r=l
                while r<len(s2) and s2[r] in need:
                    need[s2[r]] -=1


                    if(list(need.values())==[0 for x in range(len(need))]):
                        return True
                    r+=1
                
            l+=1


            need= copy.deepcopy(o_need)    
        return False