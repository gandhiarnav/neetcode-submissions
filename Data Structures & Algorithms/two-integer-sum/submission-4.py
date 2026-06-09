class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        res = []

        for i in range(len(nums)):
            hash_table[nums[i]] = i 
        print(hash_table)
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in hash_table and i != hash_table[dif]:
                return [i,hash_table[dif]]
        return []

