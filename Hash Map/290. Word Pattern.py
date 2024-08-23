class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        cMap = {}  # char to word
        wMap = {}  # word to char

        for i in range(len(pattern)):
            if pattern[i] not in cMap and words[i] not in wMap:
                cMap[pattern[i]] = words[i]  # map current char to current word
                wMap[words[i]] = pattern[i]  # map current word to current char

            else:  # already in dict
                if cMap.get(pattern[i]) != words[i] or wMap.get(words[i]) != pattern[i]:
                    return False
        return True
