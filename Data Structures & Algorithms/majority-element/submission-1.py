class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        current = float('-inf')
        for i in nums:
            if current != i:
                current = i
                count = 1
            else:
                count += 1
            if count > n//2:
                return i

            