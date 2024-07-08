# 1st approach but T.C = O(n^2)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(0, n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []

