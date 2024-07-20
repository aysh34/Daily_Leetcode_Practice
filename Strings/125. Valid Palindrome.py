class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = "".join(c for c in s if c.isalnum()).lower()
        if s2 == s2[::-1]:
            return True
        return False
