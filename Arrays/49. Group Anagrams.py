class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for i in strs:
            temp = "".join(sorted(i))

            if temp not in map:
                map[temp] = [i]
            else:
                map[temp].append(i)

        return map.values()
