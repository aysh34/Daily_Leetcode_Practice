class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        current, missing, index = 1, 0, 0
        while True:
            if index < len(arr) and arr[index] == current:
                index += 1
            else:
                # Current number is missing
                missing += 1
                if missing == k:
                    return current  # found the k-th missing integer, return it
            # Move to the next positive integer
            current += 1
