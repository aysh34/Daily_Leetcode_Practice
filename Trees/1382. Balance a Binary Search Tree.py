class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.arr = []
        self.inOrderTraversal(root)
        return self.arrToBst(0, len(self.arr) - 1)

    def inOrderTraversal(self, node):
        if not node:
            return
        self.inOrderTraversal(node.left)
        self.arr.append(node)
        self.inOrderTraversal(node.right)

    def arrToBst(self, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = self.arr[mid]
        root.left = self.arrToBst(left, mid - 1)
        root.right = self.arrToBst(mid + 1, right)
        return root

        # def inOrder(node):
        #     res = []  # a list of TreeNode objects
        #     if not node:
        #         return res
        #     return inOrder(node.left) + [node] + inOrder(node.right)

        # def arrayToBst(nodes, left, right):  # nodes == sorted array of nodes
        #     if left > right:
        #         return None

        #     m = (left + right) // 2
        #     root_node = nodes[m]  # Use the middle node directly
        #     root_node.left = arrayToBst(nodes, left, m - 1)
        #     root_node.right = arrayToBst(nodes, m + 1, right)
        #     return root_node

        # sorted_nodes = inOrder(root)
        # return arrayToBst(sorted_nodes, 0, len(sorted_nodes) - 1)
