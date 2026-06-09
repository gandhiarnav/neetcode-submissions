class Solution:
    def findMin(self, nums: List[int]) -> int:
        mi = 9999
        for i in nums:
            if mi > i:
                mi = i
        return mi
        