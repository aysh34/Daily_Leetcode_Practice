class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = {}
        for i in s:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1

        for index, item in enumerate(s):
            if mp[item] == 1:
                return index
        return -1
