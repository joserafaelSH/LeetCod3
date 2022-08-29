class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p)>len(s): return []
        
        hash_s = {}
        hash_p = {}

        for i in range(len(p)):
            if p[i] not in hash_p:
                hash_p[p[i]] = 1
            else:
                hash_p[p[i]] +=1 

            if s[i] not in hash_s:
                hash_s[s[i]] = 1
            else:
                hash_s[s[i]] +=1     




        res = []
        w = len(p)

        for i in range(len(s)-w+1):

            if len(hash_s) == len(hash_p):
                if hash_s == hash_p:
                    res.append(i)

            if hash_s[s[i]] == 1 :
                del hash_s[s[i]] 

            else:
                hash_s[s[i]] -=1

            if i == len(s)-w:
                return res

            if s[i+w] not in hash_s:
                hash_s[s[i+w]] = 1
            else:
                hash_s[s[i+w]] +=1  
        
   
