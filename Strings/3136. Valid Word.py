class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowel=False
        cons=False
        if word.isalnum():
            for i in word.lower():
                if i in 'aeiou':
                    vowel= True
                elif i.isalpha():# Ensure consonant check only considers letters
                    cons=True
        if vowel and cons:
            return True 
        return False
