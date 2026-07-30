# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        que = deque([])
        if root:
            que.append(root)
        else:
            return []
        level = 0
        while que:
            for i in range(len(que)):
                node = que.popleft()

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            level += 1
            res.append(node.val)
        return res
            

            