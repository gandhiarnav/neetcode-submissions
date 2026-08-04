class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #for finding row
        l = 0
        r = len(matrix)-1
        while l<=r:
            x = (r+l)//2
            print(x)
            print(matrix[x][0],matrix[x][-1])
            if target >= matrix[x][0] and target <= matrix[x][-1]:
                print("inside")
                #for finding cell in that row
                ll = 0
                rr = len(matrix[x])-1
                print(ll,rr)
                while ll <= rr:
                    y = (rr+ll)//2
                    if matrix[x][y] == target:
                        return True
                    elif matrix[x][y] < target:
                        ll = y + 1
                    else:
                        rr = y - 1
                return False
            elif target < matrix[x][0]:
                r = x-1
            else:
                l = x+1

        return False








        