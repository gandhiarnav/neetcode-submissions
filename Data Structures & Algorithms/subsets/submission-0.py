class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            res.extend([subset + [n] for subset in res])
        return res
        