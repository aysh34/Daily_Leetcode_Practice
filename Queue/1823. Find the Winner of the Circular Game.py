class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0  # 0-indexed
        for i in range(2, n + 1):
            winner = (winner + k) % i  # winner of current circle
        return winner + 1  # add 1 to convert back to 1-indexed
