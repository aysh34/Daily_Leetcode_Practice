class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)  # rows
        n = len(matrix[0])  # columns
        if matrix:
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == target:
                        return True
        return False
