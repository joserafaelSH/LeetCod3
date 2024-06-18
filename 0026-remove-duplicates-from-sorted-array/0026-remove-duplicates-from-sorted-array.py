class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        aux = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[aux] = nums[i]
                aux +=1

        return aux