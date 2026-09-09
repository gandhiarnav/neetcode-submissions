class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            #take
            subset.append(nums[i])
            backtrack(i+1,subset)

            #don't take
            subset.pop()
            i+=1
            while i < len(nums) and nums[i-1] == nums[i]:
                i+=1
                
            backtrack(i,subset)
        backtrack(0,[])
        return res
            