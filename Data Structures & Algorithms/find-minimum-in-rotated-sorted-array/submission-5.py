class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums)-1

        if nums[0] < nums[-1]:
            return nums[0]

        while right>=left:
            mid = (left + right)//2

            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid-1

        # return nums[left]