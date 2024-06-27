class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        x = list(set(edges[0]).intersection(set(edges[1])))
        print(x)
        return x[0]



