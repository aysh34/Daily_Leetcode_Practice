class Solution:
    def findMin(self, nums: List[int]) -> int:
        s, e = 0, len(nums) - 1
        while s < e:
            mid = (s + e) // 2
            if nums[mid] > nums[e]:
                s = mid + 1
            else:  # nums[mid] <= nums[e]
                e = mid
        return nums[
            s
        ]  # Return nums[s] or nums[e], whichever points to the minimum element
