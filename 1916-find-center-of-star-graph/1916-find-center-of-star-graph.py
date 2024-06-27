class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        vertex_freq = {}
        for pair in edges:
            if pair[0] in vertex_freq:
                vertex_freq[pair[0]] +=1
            else: 
                vertex_freq[pair[0]] = 1
            
            if pair[1] in vertex_freq:
                vertex_freq[pair[1]] +=1
            else: 
                vertex_freq[pair[1]] = 1
        
        max = -1 
        idx_max = 1
        for key, val in vertex_freq.items():
            if val > max:
                max = val
                idx_max = key
        
        return idx_max