class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"

        stack = []
        for i in num:
            while stack and stack[-1] > i and k > 0:
                stack.pop()
                k -= 1
            stack.append(i)

        # stack = stack[:-k] if k else stack
        # this flag is helpful in situations like num ="11" and k = 1
        while k > 0:  # after for loop if still k > 0
            stack.pop()
            k -= 1

        res = "".join(stack).lstrip("0")
        return res if res else "0"