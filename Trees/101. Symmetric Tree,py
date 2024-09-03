# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(
        self, root: Optional[TreeNode]
    ) -> bool:  # The left subtree is a mirror reflection of the right subtree.
        if not root:  #  Base Case: Empty Tree
            return True
        left, right = root.left, root.right

        def isMirrorReflection(left, right):

            if left == None and right == None:
                return True
            if left == None or right == None:
                return False
            if left.val != right.val:
                return False

            return isMirrorReflection(left.left, right.right) and isMirrorReflection(
                left.right, right.left
            )

        return isMirrorReflection(left, right)
