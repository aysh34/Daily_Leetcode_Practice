class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s = sentence.split()
        set1 = set(dictionary)
        for i in range(len(s)):
            for j in set1:
                if s[i].startswith(j):
                    s[i] = j
        return " ".join(s)
