class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst = []
        for i in matrix:
            for j in i:
                lst.append(j)
        print(lst)
        l = 0
        r = len(lst)-1
        while l <= r:
            mid = (l+r)//2
            if lst[mid] == target:
                return True
            elif lst[mid] < target:
                l = mid + 1
            else:
                r = mid-1
        return False
