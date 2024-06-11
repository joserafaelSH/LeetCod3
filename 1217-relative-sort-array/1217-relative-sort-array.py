class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        memo = [0 for i in range(1001)]
        response = []
        for i in arr1:
            memo[i]+=1
        
        for i in arr2:
            response += [i for k in range(memo[i])]
            memo[i] = 0

        aux = []
        for i in range(len(memo)):
            if memo[i] != 0:
                aux+=[i for k in range(memo[i])]


        aux.sort()

        return response + aux 