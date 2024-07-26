class Solution:
    def scoreOfString(self, s: str) -> int:
        # ord() fun returns ascii values
        diff = 0
        for i in range(1, len(s)):
            diff += abs(ord(s[i - 1]) - ord(s[i]))
        return diff


# for i in range(len(s)-1):
#   score += abs(ord(s[i]) - ord(s[i+1]))
