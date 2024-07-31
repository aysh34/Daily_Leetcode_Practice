class Solution:
    def arrangeCoins(self, n: int) -> int:
        s = 0
        for i in range(1, n + 1):
            s += i
            if s > n:
                return i - 1
        return i


# Using the quadratic formula to solve for k
# k = int((-1 + math.sqrt(1 + 8 * n)) // 2)
# return k
