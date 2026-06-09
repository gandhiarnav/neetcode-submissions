class Solution:
    def bs(self, nums, target,l,r):
        
        
        while r>=l:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

        return -1
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums)-1

        if nums[0] < nums[-1]:
            return 0

        while right>=left:
            mid = (left + right)//2

            if nums[mid - 1] > nums[mid]:
                return mid
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid-1
    def search(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1
        pivot = self.findMin(nums)

        if nums[pivot] <= target <= nums[-1]:
            return self.bs(nums,target,pivot,len(nums)-1)
        else:
            return self.bs(nums,target,0,pivot-1)

        