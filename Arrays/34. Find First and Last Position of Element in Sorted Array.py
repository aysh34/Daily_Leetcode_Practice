class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == target:
                if nums[r] != target:
                    r -= 1
                else:
                    return [l, r]
                    break
            else:
                l += 1
        return [-1, -1]
