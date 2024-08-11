class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if (
                    not stack
                    or (stack[-1] != "(" and i == ")")
                    or (stack[-1] != "{" and i == "}")
                    or (stack[-1] != "[" and i == "]")
                ):
                    return False
                stack.pop()

        return not stack  # return true if stack is empty else false
