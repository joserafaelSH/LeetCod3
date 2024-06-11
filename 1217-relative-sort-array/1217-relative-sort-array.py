class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        memo = [0 for i in range(1001)]
        aux = []
        response = []

        for i in arr1:
            if i not in arr2:
                aux.append(i)

        for i in arr2:
            for k in arr1:
                if k == i:
                    response.append(k)

        aux.sort()

        return response + aux 