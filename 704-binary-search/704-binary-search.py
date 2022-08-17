class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        s0 = 0
        s = len(nums)-1
        
        while s0 <= s:
            mid = (s+s0)//2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                s = mid-1
            else:
                s0 = mid+1 

        return -1