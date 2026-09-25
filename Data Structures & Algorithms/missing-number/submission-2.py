class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        
        n = max(nums)
        
        expected_s = n*(n+1)//2
        dif = expected_s - s
        if dif == 0:
            m = min(nums)
            if m == 0:
                return n+1
            return 0
        else:
            return dif