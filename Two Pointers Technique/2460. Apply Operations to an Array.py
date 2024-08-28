class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0

        nonzero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonzero] = nums[i]
                nonzero += 1
        for i in range(nonzero,len(nums)):
            nums[i] = 0

        return nums
        
        # result = []
        # for num in nums:
        #     if num != 0:
        #         result.append(num)
        # zeros_to_add = n - len(result)
        # result.extend([0] * zeros_to_add)
        # return result