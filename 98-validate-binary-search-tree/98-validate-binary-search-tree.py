# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        def isValidBST(self, root: Optional[TreeNode]) -> bool:
            res = []
            head = root 

            def fn(root):
                if root:
                    fn(root.left)
                    res.append(root.val)
                    fn(root.right)

            fn(root)

            for i in range(len(res)-1):

                if res[i+1]<=res[i]:
                    return False

            return True

   
                    
     
            