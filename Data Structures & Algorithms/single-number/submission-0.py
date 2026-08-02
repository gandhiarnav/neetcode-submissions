class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = int()
        nums.sort()
        nums.append(528291)
        print(nums)
        
        for i in range(0,len(nums),2):
            print(i)
            if nums[i] != nums[i+1]:
                return nums[i]
            

