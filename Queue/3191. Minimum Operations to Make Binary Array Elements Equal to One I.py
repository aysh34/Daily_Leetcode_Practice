class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for i in range(len(nums) - 2):
            if nums[i] != 0:
                continue
            nums[i] = 1 - nums[i]
            nums[i + 1] = 1 - nums[i + 1]
            nums[i + 2] = 1 - nums[i + 2]
            operations += 1

        if nums[-1] == 0 or nums[-2] == 0:  # check last and 2nd last element
            return -1
        return operations
