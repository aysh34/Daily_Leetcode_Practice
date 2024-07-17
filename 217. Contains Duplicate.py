class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 1st approach:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    
        # 2nd approach
        if len(nums) == len(set(nums)):
            return False
        return True
   
        # 3rd approach 
        return len(set(nums)) < len(nums)
