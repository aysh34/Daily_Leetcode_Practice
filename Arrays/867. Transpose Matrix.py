class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        #    Initialize the transposed matrix with dimensions cols x rows
        transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                transposed_matrix[j][i] = matrix[i][j]

        return transposed_matrix

    # return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
