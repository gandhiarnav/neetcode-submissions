class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n_dict={}
        for i in nums:
            if i in n_dict:
                return True
            else:
                n_dict[i]=1
        return False


obj = Solution()

nums=[]
print(obj.hasDuplicate(nums))