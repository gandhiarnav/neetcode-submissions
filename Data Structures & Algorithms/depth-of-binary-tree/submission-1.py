# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        
        stack = deque([root])
        while stack:
            
            for i in range(len(stack)):
                itr = stack.popleft()
                if itr.left:
                    stack.append(itr.left)
                if itr.right:
                    stack.append(itr.right)
            level+=1

        return level