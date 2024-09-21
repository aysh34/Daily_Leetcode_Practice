class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            rowSet = set()
            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] in rowSet:
                        return False
                    else:
                        rowSet.add(board[row][col])

        for col in range(9):
            colSet = set()
            for row in range(9):
                if board[row][col] != ".":
                    if board[row][col] in colSet:
                        return False
                    else:
                        colSet.add(board[row][col])

        for sr in range(0, 9, 3):
            er = sr + 3
            for sc in range(0, 9, 3):
                ec = sc + 3
                if not self.checkSubgrid(board, sr, er, sc, ec):
                    return False

        return True

    def checkSubgrid(self, board: List[List[str]], sr, er, sc, ec):
        s = set()
        for row in range(sr, er):
            for col in range(sc, ec):
                if board[row][col] != ".":
                    if board[row][col] in s:
                        return False
                    else:
                        s.add(board[row][col])

        return True
        
