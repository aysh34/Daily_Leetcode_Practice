class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = [""] * len(s)
        for i, char in enumerate(s):
            l[indices[i]] = char
        return "".join(l)

        # The zip function in Python is used to combine multiple iterables
        #  shuffled = [''] * len(s)
        # for i, char in zip(indices, s):
        #     shuffled[i] = char
        # return ''.join(shuffled)


        #     list.insert(index, element)
        #     l1.pop(index)
        #     del l1[j]
