class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        if len(s1)==1:
            return True if s1 in s2 else False
        
        hash1 = {}
        hash2 ={}
        
        for i in range(len(s1)):
            if s1[i] in hash1:
                hash1[s1[i]] +=1 
            else:
                hash1[s1[i]] =1 
            
            if s2[i] in hash2:
                hash2[s2[i]] +=1 
            else:
                hash2[s2[i]] =1 
        

        w = len(s1) 
        
        for i in range(0,len(s2)-w+1):
            
            if len(hash1) == len(hash2):
                if hash1 == hash2:
                    return True
            
            if s2[i] in hash2:
                if hash2[s2[i]] == 1:
                    del hash2[s2[i]]
                else:
                    hash2[s2[i]] -=1
            
            if i == len(s2)-w:
                return False 
            
            if s2[i+w] not in hash2:
                hash2[s2[i+w]] = 1
            else:
                hash2[s2[i+w]] +=1
                
                
            
            
                  
                
                
            
        
        
        