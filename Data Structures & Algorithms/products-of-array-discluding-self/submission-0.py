class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            mul=1
            for j in range(len(nums)):
                if j != i:
                    mul*=nums[j]
            output.append(mul)
        
        return output
