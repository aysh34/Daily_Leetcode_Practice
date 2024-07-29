class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ev = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                ev += 1
        return ev


# To find the length of a number (i.e., the number of digits) convert the number to a string and then measure the length of that string.
