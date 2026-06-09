class Solution:
    def bs(self, nums, ele):
        l = 0
        r = len(nums)-1
        while r>=l:
            mid = (l+r)//2
            print(mid,ele)
            if nums[mid] == ele:
                return mid
            elif nums[mid] > ele:
                r = mid-1
            else:
                l = mid+1

        return -9999

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,n in enumerate(numbers):
            diff = target - n

            if diff in numbers:
                return [i+1,self.bs(numbers,diff)+1]
