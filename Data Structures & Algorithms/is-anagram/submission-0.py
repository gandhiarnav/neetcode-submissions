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
s= str()
t= str()
obj = Solution()
result = obj.isAnagram(s,t)
print(result)
            