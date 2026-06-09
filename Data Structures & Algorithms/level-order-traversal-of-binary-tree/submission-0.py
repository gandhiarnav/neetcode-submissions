# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = deque([root])
        level = 0
        while stack:
            temp = []
            for i in range(len(stack)):
                itr = stack.popleft()
                temp.append(itr.val)
                if itr.left:
                    stack.append(itr.left)
                if itr.right:
                    stack.append(itr.right)
            level+=1
            res.append(temp)


        return res