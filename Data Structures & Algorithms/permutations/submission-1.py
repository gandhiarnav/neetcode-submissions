class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(per,pick):
            if len(per) == len(nums):
                res.append(per.copy())
                return 
            
            for i in range(len(nums)):
                if not pick[i]:
                    per.append(nums[i])
                    pick[i] = True
                    print("backtrack(",per,',',pick,")")
                    backtrack(per,pick)
                    per.pop()
                    pick[i] = False
            return

            
        backtrack([],[False for x in nums])
        return res
