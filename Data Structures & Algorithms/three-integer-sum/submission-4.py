class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        res = []
        nums.sort()
        while i < len(nums):
            l = i+1
            r = len(nums) - 1
            
            while l<r: 
                sum = nums[i]+ nums[l] +nums[r]
                if sum == 0:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l+=1
                elif sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1

            i+=1
        return res
            
