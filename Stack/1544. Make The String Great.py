class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and char.lower() == stack[-1].lower() and char != stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
