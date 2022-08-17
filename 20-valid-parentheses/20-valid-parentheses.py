class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque 
        
        if len(s) == 1:
            return False
        
        q = deque([])
        
        for i in s:
            if i == ")":
                if len(q)==0 or q.pop() != "(":
                    return False
            
            elif i == "]":
                if len(q)==0 or q.pop() != "[":
                    return False
            
            elif i == "}":
                if len(q)==0 or q.pop() != "{":
                    return False
            
            else:
                q.append(i)
        
        if len(q) > 0:
            return False
        else:
            return True
                
            