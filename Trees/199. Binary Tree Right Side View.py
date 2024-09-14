
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
    # dfs approach
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #    self.rightSide = []
    #     self.dfs(root,0)
    #     return self.rightSide

    # def dfs(self,node,depth):
    #     if not node:
    #         return []
               
    #     if depth == len(self.rightSide):
    #         self.rightSide.append(node.val)
        
    #     self.dfs(node.right,depth+1)
    #     self.dfs(node.left,depth+1)

    #     return self.rightSide

