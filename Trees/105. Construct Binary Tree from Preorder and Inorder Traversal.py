# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = [0]  # list --> so that it gets updated in each recersive call
        n = len(inorder)
        hashmap = {val : indx for indx, val in enumerate(inorder)} # preprocess inorder into a hashmap {value: index}

        return self.solve(preorder, hashmap, 0, n - 1, idx)

    def solve(self, preorder, hashmap, start, end, idx):  # recersive func
        if start > end:
            return None

        root = preorder[idx[0]]
        node = TreeNode(root)

        # i = start
        # while i <= end:  # on inorder array
        #     if inorder[i] == root:
        #         break  # at the end i will be the index of root in inorder array
        #     i += 1
        
        root_indx = hashmap[root] # constt time lookup

        idx[0] += 1  # move on to next element/root in preorder array

        node.left = self.solve(preorder, hashmap, start, root_indx - 1, idx)
        node.right = self.solve(preorder, hashmap, root_indx + 1, end, idx)

        return node
