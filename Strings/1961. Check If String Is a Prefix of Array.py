class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:

# To concatenate strings one by one from an array use a loop to iterate through each string in the array and keep appending it to a result string. 
        res=""
        for i in words:
            res+=i # append curr string in res
            if s==res:
                return True
        return False
            