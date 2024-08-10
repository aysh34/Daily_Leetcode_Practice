class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != "]":
                stack.append(i)
                continue

            string = ""
            while stack and stack[-1] != "[":
                string = stack.pop() + string
            stack.pop()  # pop [

            mul = ""
            while stack and stack[-1].isdigit():  # in case 100[leetcode]
                mul = stack.pop() + mul  # "100"

            stack.append(int(mul) * string)
        return "".join(stack)
