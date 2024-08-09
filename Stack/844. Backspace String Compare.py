class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def newStr(inputStr):
            stack = []
            for i in inputStr:
                if i == "#":
                    if stack:  # stack is not None
                        stack.pop()
                else:  # if not "#"
                    stack.append(i)
            return "".join(stack)

        return newStr(s) == newStr(t)
