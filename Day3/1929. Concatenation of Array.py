class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.append(i)
        for i in nums:
            ans.append(i)
        return ans

        # 2nd approach
        nums.extend(nums)
        return nums

        return nums + nums  # Concatenate the list with itself
        return nums * 2  # Repeat the list twice
