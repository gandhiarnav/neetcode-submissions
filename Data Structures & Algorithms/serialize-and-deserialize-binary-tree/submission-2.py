# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ""

        res = []

        stack = deque([root])

        while stack:
            itr = stack.popleft()

            if itr:
                #check if str is needed 
                res.append(str(itr.val))
                stack.append(itr.left)
                stack.append(itr.right)
            else:
                res.append("N")
        print(",".join(res))
        print(not(""))
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        lst = data.split(",")
        print(lst)
        
        root = TreeNode(int(lst[0]))
        print(f"{lst[0]} added")
        stack = deque([root])
        i = 1
        while stack and i<len(lst):
            itr = stack.popleft()
            if lst[i] != 'N':
                itr.left = TreeNode(lst[i])
                print(f"{lst[i]} added")
                stack.append(itr.left)
                
            i+=1
            if lst[i] != 'N':
                itr.right = TreeNode(lst[i])
                print(f"{lst[i]} added")
                stack.append(itr.right)
            i+=1

        return root
