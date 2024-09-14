
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        que = deque() 
        que.append(root)
        rightSideView = []

        while que: # level order traversal
            level_size = len(que)

            for i in range(level_size):
                node = que.popleft()    
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                if i == level_size - 1:
                    rightSideView.append(node.val) # ensure we only append the rightmost node of each level
               
            # rightSideView.append(node.val)
        
        return rightSideView
