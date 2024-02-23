class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0]) if matrix else 0
        rows_to_zero=set()
        cols_to_zero=set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)
        for i in rows_to_zero:
            matrix[i]=[0]*col
        for j in cols_to_zero:
            for i in range(row):
                matrix[i][j]=0
        return matrix
