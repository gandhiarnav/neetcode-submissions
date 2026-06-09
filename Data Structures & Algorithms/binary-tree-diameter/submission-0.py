# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxPath = 0
        def dfs(node):
            if not node:
                return 0
            
            maxPathLeft = dfs(node.left)
            maxPathRight = dfs(node.right)

            self.maxPath = max(self.maxPath,maxPathLeft + maxPathRight)
            print(self.maxPath)
            return max(maxPathLeft,maxPathRight) + 1

        dfs(root)
        
        return self.maxPath



