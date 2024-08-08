class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = [s[0]]
        c = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                c += 1
            else:
                c = 1
            if c < 3:
                stack.append(s[i])
        return "".join(stack)
