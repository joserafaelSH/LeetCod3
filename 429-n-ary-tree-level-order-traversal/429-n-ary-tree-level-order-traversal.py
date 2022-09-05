"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
            
            for n in curr.children:
                queue.append(n)
            
            h-=1
            if h == 0:
                res.append(l)
                l = []
                h = len(queue)
    
        return res