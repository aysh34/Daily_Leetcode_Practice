class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        m = []
        prev = 0
        for space in spaces:
            m.append(s[prev:space]) # substring before the space
            m.append(" ") 
            prev = space
        m.append(s[prev:]) # add the remaining part of the string
        return "".join(m)

        # m = []
        # p = 0
        # for i in range(0,len(s)):
        #     if p < len(spaces) and i == spaces[p]: # condition -> p must be in bound
        #         m.append(" ")
        #         p += 1
        #     m.append(s[i])
        # return "".join(m)
