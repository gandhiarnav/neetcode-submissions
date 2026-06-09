class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                    return True
                else:
                    pass
        return False
       
nums = []

obj = Solution()
result = obj.hasDuplicate(nums)

print(result)
