class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        p = 0
        for i in nums:
            if i in count:
                p += count[i]
                count[i] += 1
            else:
                count[i] = 1
        return p

        # p = 0
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j] and i<j:
        #             p += 1
        # return p
