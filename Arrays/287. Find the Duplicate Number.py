class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)  # O(n log n)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
        return -1

        # tortoise and hare (Floyd's cycle detection) algorithm, which operates on O(N)
