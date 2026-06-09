# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        lst=[]
        self.inOrder(root,lst)
        print(lst)
        j=0
        for i in range(1,len(lst)):
            if lst[j] == lst[i]:
                return False
            j+=1


        if sorted(lst) == lst:
            return True
        else:
            return False



    def inOrder(self,root ,lst ):
        if root:
            if root.left:
                self.inOrder(root.left,lst)

            lst.append(root.val)

            if root.right:
                self.inOrder(root.right,lst)

        

        
        
