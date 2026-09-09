class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(per,temp_lst=[]):
            if len(per) >= len(nums):
                res.append(per.copy())
                return
            
            for i in range(len(nums)):
                if temp_lst[i]:
                    continue
                else:
                    per.append(nums[i])
                    temp_lst[i] = True
                    dfs(per,temp_lst)
                    temp_lst[i] = False
                    per.pop()


        dfs([],[False for x in nums])
        return res
            




