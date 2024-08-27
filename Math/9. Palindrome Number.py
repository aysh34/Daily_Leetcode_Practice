class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        orig = x  # 123
        reverse = 0
        while x != 0:
            digit = x % 10  # 3
            reverse = reverse * 10 + digit
            x = x // 10
        return orig == reverse

        # s = str(x)
        # return s == s[::-1]
