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
                print(plst)
                if itr.right:
                    pqueue.append(itr.right)
                else:
                    plst.append("no_right")
                print(plst)
        
        while qqueue:
            for i in range(len(qqueue)):
                itr = qqueue.popleft()
                qlst.append(itr.val)
                if itr.left:
                    qqueue.append(itr.left)
                else:
                    qlst.append("no_left")
                print(qlst)
                if itr.right:
                    qqueue.append(itr.right)
                else:
                    qlst.append("no_right")
                print(qlst)

        if len(plst) != len(qlst):
            return False


        if plst == qlst:
            return True
        else:
            return False
                

            