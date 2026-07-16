# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxNum):
            res = 0
            
            if not node:
                return 0
            print(node.val)
            if node.val >= maxNum:
                res = 1
            else:
                res = 0

            maxNum = max(maxNum, node.val)
                
            res+= dfs(node.left,maxNum) + dfs(node.right,maxNum)            

            return res

        return dfs(root, root.val)
