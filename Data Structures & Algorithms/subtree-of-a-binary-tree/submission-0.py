# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False

        pqueue = deque([p])
        plst = []
        qqueue = deque([q])
        qlst = []
        while pqueue:
            for i in range(len(pqueue)):
                itr = pqueue.popleft()
                plst.append(itr.val)
                if itr.left:
                    pqueue.append(itr.left)
                else:
                    plst.append("no_left")
                
                if itr.right:
                    pqueue.append(itr.right)
                else:
                    plst.append("no_right")
                
        
        while qqueue:
            for i in range(len(qqueue)):
                itr = qqueue.popleft()
                qlst.append(itr.val)
                if itr.left:
                    qqueue.append(itr.left)
                else:
                    qlst.append("no_left")
                
                if itr.right:
                    qqueue.append(itr.right)
                else:
                    qlst.append("no_right")
                

        if len(plst) != len(qlst):
            return False


        if plst == qlst:
            return True
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                itr = queue.popleft()
                if self.isSameTree(itr,subRoot):
                    return True
                if itr.left:
                    queue.append(itr.left)
                if itr.right:
                    queue.append(itr.right)
        return False










