class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        t=[i[::-1] for i in s]
        return " ".join(t)

        # TC: o(n)
        # SC: o(n)