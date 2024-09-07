# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.rootToLeaf(root, 0)

    def rootToLeaf(self, root, cur):
        if not root:
            return 0

        cur = (cur * 10) + root.val

        if not root.left and not root.right:  # leaf node
            return cur
        else:
            l = self.rootToLeaf(root.left, cur)
            r = self.rootToLeaf(root.right, cur)

        return l + r
