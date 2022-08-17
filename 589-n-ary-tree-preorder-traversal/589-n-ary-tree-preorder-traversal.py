"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res =[]
        if root is None:
            return root 
        
        if root.children is None:
            return root.val
        else:
            x = 0
            head = root
            filhos = head.children
            res.append(head.val)
            for i in filhos:
                x = self.preorder(i)
                res+=x
                
                 

        return res