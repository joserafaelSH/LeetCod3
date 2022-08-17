class Solution:
    def longestPalindrome(self, s: str) -> int:

        if len(s) == 1:
            return 1
    
        hash = {}
        for i in s:
            if i in hash:
                hash[i] +=1
            else:
                hash[i] = 1
        
        c = 0

        impar = 0
        for k,v in hash.items():
            if v > 1:
                if v % 2 == 0:
                    c+=v
                else:
                    c+= v-1
                    impar+=1
            else:
                impar+=1
                
        return c+1 if impar>0 else c