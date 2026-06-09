class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_p=1
        cur_p=1
        print(nums)
        if len(nums)==0:
            return 0
        n_set=set()
        for i in nums:
            n_set.add(i)
        print(n_set)
        min_nums = [ x for x in n_set]
        min_nums.sort()
        print(min_nums)
        for i in range(1,len(min_nums)):
            if min_nums[i-1]+1 == min_nums[i]:
                cur_p+=1 
                if max_p < cur_p:
                    max_p=cur_p
            else:
                cur_p=1
            
        return max_p
        