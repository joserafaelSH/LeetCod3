class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash = {}
        for i in range(len(s)): 
            if s[i] not in hash:
                hash[s[i]] = t[i]
            else:
                if hash[s[i]] != t[i]:
                    return False
               
        hash2 = {val: key for key, val in hash.items()}
        
        if len(hash) != len(hash2):
            return False 
        
        return True
        
      