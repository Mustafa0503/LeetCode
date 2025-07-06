class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_zero=set()
        col_zero=set()
        r=len(matrix)
        c=len(matrix[0])
        #to find the row and columns
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    row_zero.add(i)
                    col_zero.add(j)
        #make the rows zero
        for i in row_zero:
            matrix[i]=[0]*c

        #make the columns zero
        for j in col_zero:
            for i in range(r):
                matrix[i][j] = 0
        
        return matrix