class Solution:
    def search(self, num: List[int], target: int) -> int:
        l = 0
        r = len(num)-1
        
        while r>=l:
            mid = (l+r)//2
            if num[mid] == target:
                return mid
            elif num[mid] > target:
                r = mid - 1
            else:
                l = mid + 1 

        return -1