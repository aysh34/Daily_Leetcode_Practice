class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a map where the key is a representation of the sorted version of the word (this helps identify if two words are anagrams). The value of each key is a list of all the anagrams of the key.
        map = {}

        for i in strs:
            temp = "".join(sorted(i))

            if temp not in map:
                map[temp] = [i]
            else:
                map[temp].append(i)

        return map.values()
