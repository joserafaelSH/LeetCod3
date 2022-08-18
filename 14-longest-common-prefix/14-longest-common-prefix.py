class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        
        i = 0
        resp= ""
        if not strs[0]:
            return resp
        
      
        base = strs[0]
        
        for i in range(len(base)):
            for s in strs:
                if i == len(s) or s[i] != base[i]:
                    return resp
            resp+=base[i]
        
        return resp