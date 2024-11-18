class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # for i in range(0, n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #                 return [i,j]
        # return [] # TC: O(n^2)

        map = {}  # TC: O(n)
        for i in range(0, len(nums)):
            remaining = target - nums[i]
            if remaining in map:
                return [map[remaining], i]
            else:
                map[nums[i]] = i
