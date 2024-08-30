class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the first pair where nums[i] < nums[i + 1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i == -1:
            nums = nums.reverse()
            return nums

        # Find the smallest number greater than nums[i] to the right of i
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1

        # Swap the numbers at i and j
        nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1 :] = nums[i + 1 :][::-1]

        return nums
