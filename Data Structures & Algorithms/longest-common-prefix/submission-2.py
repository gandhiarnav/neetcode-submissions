class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        fw = strs[0]
        i = 0
        ctr = 0
        for k in strs:
            if k == fw:
                ctr += 1
            else:
                break
        if ctr == len(strs):
            return k
           
        try:
            for i in range(len(fw)):
                # flag = True
                for j in strs:
                    if j[i] != fw[i]:
                        if i > 0:
                            return fw[0:i]
                        else:
                            return ""
            if i > 0:
                return fw[0:i+1]                
            else:
                return "" 
        except IndexError:
                if i > 0:
                    return fw[0:i]
                else:
                    return ""  
            

        