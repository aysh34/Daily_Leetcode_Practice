class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #  maximize the sum of the minimums
        nums.sort()
        mx = 0
        for i in range(0, len(nums), 2):
            mx += nums[i]
        return mx
