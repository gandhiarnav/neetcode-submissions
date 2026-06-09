# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        self.maxSum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Path passing through this node
            current = node.val + left + right

            self.maxSum = max(self.maxSum, current)

            # Return best single-branch path
            return node.val + max(left, right)

        dfs(root)
        return self.maxSum
        