class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Palindromes can have at most one character with an odd frequency (this character can be in the middle), while all other characters must have even frequencies.
        from collections import Counter

        pairs = Counter(s)  # Count the frequency of each character in the string
        l = 0
        odd = False
        for count in pairs.values():
            if count % 2 == 0:
                l += count
            else:
                l += count - 1
                odd = True
        if odd:
            l += 1  # Add 1 to the length if any character with an odd count found
        return l
