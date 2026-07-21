class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        self.mprint(matrix)

        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                



    def mprint(self,mat):
        n = len(mat)
        for i in range(n):
            for j in range(n):
                print(mat[i][j],end = ' ')
            print()
        