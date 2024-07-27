class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  
        # TC: O(n)  
        d = set()
        i, j, length = 0, 0, 0
        while j < len(s):
            while s[j] in d: 
                d.remove(s[i])
                i += 1
            d.add(s[j])
            length = max(length, j - i + 1) 
            j += 1
        return length


        # TC = O(n3)
        # maxLen=0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         # l.append(s[i,j+1])
        #         sub=s[i:j+1]
        #         st=set(sub)
        #         # st.add(sub)
        #         if len(sub) == len(st):
        #             maxLen = max(maxLen, len(sub))
        # return maxLen
