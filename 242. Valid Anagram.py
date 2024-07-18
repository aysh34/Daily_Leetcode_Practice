class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # conditions --> 2
        # must have same length
        # must have same characters in same frequency

        # if len(s)!=len(t):
        #     return False
        # return sorted(s)==sorted(t)

        from collections import Counter 
        return Counter(s)== Counter(t)
         # Counter creates a dictionary-like object where the keys are the characters and the values are the counts of those characters
