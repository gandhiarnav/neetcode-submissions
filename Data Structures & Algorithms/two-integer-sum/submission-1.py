class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(0,l):
            for j in range(i+1,l):
                if nums[i]+nums[j]==target:
                    return [i,j]
        else:
            return "Pair doesn't exist"



nums = []
target = int

obj = Solution()
result = obj.twoSum(nums,target)
print(result)        