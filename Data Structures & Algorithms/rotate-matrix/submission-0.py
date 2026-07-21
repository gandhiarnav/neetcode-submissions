class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end = ' ')
            print()
        
        for i in range(n-1):
            for j in range(i+1,n):
                if i!=j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp

        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end = ' ')
            print()

        for i in range(n):
            for j in range(0,n//2):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[i][n-j-1]
                    matrix[i][n-j-1] = temp
                    
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end = ' ')
            print()



