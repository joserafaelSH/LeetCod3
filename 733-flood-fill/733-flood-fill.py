class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        
        start_color = image[sr][sc] 
        from collections import deque
        
        vertex = deque([])
        
        if color == start_color:
            return image 
        
        image[sr][sc] =color
        
        
        
        def verificar(sr,sc):
            vertex = deque([])
        
            if sr > 0: 
                if image[sr-1][sc] == start_color:
                    vertex.appendleft([sr-1,sc])

            if sr < m-1:
                if image[sr+1][sc] == start_color:
                    vertex.appendleft([sr+1,sc])

            if sc < n-1:
                if image[sr][sc+1] == start_color:
                    vertex.appendleft([sr,sc+1])

            if sc > 0:
                if image[sr][sc-1] == start_color:
                    vertex.appendleft([sr,sc-1])
        
            
            return vertex
        
        vertex=verificar(sr,sc)
      
        while len(vertex) > 0:
            v = vertex.popleft()
            image[v[0]][v[1]] = color
            vertex+=(verificar(v[0], v[1]))
                
        return image