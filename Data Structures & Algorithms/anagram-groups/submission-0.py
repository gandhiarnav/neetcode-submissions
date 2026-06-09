class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        j_dict={}

        for i in s:
            if i in s_dict:
                s_dict[i]+=1
            else:
                s_dict[i]=1
            
        for j in t:
            if j in j_dict:
                j_dict[j]+=1
            else:
                j_dict[j]=1
    
        if s_dict == j_dict:
            return True
        else:
            return False
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out=[]
        done=set()
        for i in range(len(strs)):
            app=[]
            if strs[i] in done:
                    continue
            app.append(strs[i])
            
            for j in range(i+1,len(strs)):
                
                
                if self.isAnagram(app[0],strs[j]):
                    app.append(strs[j])
                    done.add(strs[j])
                    
                    
            out.append(app)
        return(out)
        
strs=[]
obj = Solution()
result = obj.groupAnagrams(strs)
print(result)
            









        