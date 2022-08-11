class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        somaR= sum(nums)
        somaL = 0
        for i, val in enumerate(nums):
            if somaL == somaR - val - somaL:
                return i
            somaL+=val

        return -1