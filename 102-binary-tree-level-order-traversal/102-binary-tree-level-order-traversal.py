# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        from collections import deque
        
        res = []
        l = []
        queue = deque([root])
    
        if root is None:
            return None
        
        h =1 
        while len(queue) !=0:
            curr = queue.popleft()
            l.append(curr.val)
        
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)

            h-=1
            if h == 0:
                res.append(l)
                l = []
                h = len(queue)
    
        return res