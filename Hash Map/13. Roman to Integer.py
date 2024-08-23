class Solution:
    def romanToInt(self, s: str) -> int:
        m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integer = 0
        for i in range(len(s)):
            if (
                i < len(s) - 1 and m[s[i]] < m[s[i + 1]]
            ):  #  The key observation is that when a smaller numeral appears before a larger one subtract it.
                integer -= m[s[i]]
            else:
                integer += m[s[i]]
        return integer
