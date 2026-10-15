class Solution:
    def rob(self, nums: List[int]) -> int:
        n =  len(nums)
        if n == 1:
            return nums[0]
        def help(nums):
            rob1,rob2 = 0,0
            for i in range(len(nums)):
                temp = rob1
                rob1 = rob2
                rob2 = max(rob1,nums[i] + temp)
            return rob2

        return max(help(nums[0:n-1]),help(nums[1:n]))
