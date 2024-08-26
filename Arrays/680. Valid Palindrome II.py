class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            # else:
            #     return s[l+1:r+1] == s[l+1:r+1][::-1] or r[l:r] == r[l:r][::-1]
            if s[l] != s[r]:
                left = s[l + 1 : r + 1]  # remove left element
                reverse_left = left[::-1]
                right = s[l:r]  # remove right element
                reverse_right = right[::-1]
                return left == reverse_left or right == reverse_right
        return True
