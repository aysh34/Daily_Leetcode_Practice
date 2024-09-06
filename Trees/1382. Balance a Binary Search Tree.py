class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inOrder(node):
            # res --> a list of TreeNode objects.It’s just a list of nodes arranged in the sequence they should appear in a balanced BST.
            res = []
            if not node:
                return res
            res.extend(inOrder(node.left))
            res.append(node)  # Append the actual node, not just the value
            res.extend(inOrder(node.right))
            return res

            # if not node:
            #     return []
            # return inOrder(node.left) + [node.val] + inOrder(node.right)

        def arrayToBst(nodes, left, right):  # nodes == sorted array of nodes
            if left > right:
                return None

            m = (left + right) // 2
            root_node = nodes[m]  # Use the middle node directly
            root_node.left = arrayToBst(nodes, left, m - 1)
            root_node.right = arrayToBst(nodes, m + 1, right)
            return root_node

        # def arrayToBst(sorted_array, left, right):
        #     if left > right:  # Base case to stop recursion
        #         return None
        # m = (left + right) // 2

        # new_node = TreeNode(sorted_array[m])
        # new_node.left = arrayToBst(sorted_array, left, m - 1)
        # new_node.right = arrayToBst(sorted_array, m + 1, right)
        # return new_node

        sorted_nodes = inOrder(root)
        return arrayToBst(sorted_nodes, 0, len(sorted_nodes) - 1)
