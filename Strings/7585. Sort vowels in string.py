class Solution:
    def sortVowels(self, s: str) -> str:
        # vowels=[]
        # for i in range(len(s)):
        #     if s[i] in 'aeiouAEIOU':
        #         vowels.append(s[i])

        vowels = [v for v in s if v in "aeiouAEIOU"]  # extract vowels
        vowels = sorted(vowels)  # sort by ascii values
        v = []
        ind = 0
        for j in s:
            if j in "aeiouAEIOU":
                v.append(vowels[ind])  # add vowel in the new list
                ind += 1
            else:
                v.append(j)  # consonant
        return "".join(v)

    #    TC & SC : O(n)
