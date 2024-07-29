class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = list(set(nums))
        if len(l) >= 3:
            l = sorted(l, reverse=True)
            return l[2]
        else:
            return max(l)  # length <3
