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


# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         match = {")": "(", "}": "{", "]": "["}
#         for i in s:
#             if i in "({[":
#                 stack.append(i)  # push in stack
#             elif i in ")}]":
#                 # either stack is empty or top/opening brac of the stack != respective opening brac
#                 if (
#                     not stack or stack[-1] != match[i]
#                 ):  # match[i] == opening brac and i == closing brac
#                     return False
#                 else:
#                     stack.pop()

#         return len(stack) == 0
