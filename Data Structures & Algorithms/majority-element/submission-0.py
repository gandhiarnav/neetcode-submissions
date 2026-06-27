class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        n = len(nums)
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
            
            if dict[i] > n//2:
                return i
            