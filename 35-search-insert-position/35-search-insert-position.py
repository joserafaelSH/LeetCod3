class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1:
            if nums[0] >= target:
                return 0
            else: return 1
        
        s0 = 0
        s = len(nums)-1
        idx = 0
        
        
        while s0 <= s:
            mid = (s+s0)//2
            if nums[mid] == target: 
                idx =  mid
                break

            if nums[mid] > target:
                idx = mid
                s = mid-1
                
                
            else:
                idx = mid
                s0 = mid+1 
                
        
        if idx == 0:
            if nums[0] >= target:
                return 0
            else:
                return 1
        
        if nums[idx] ==target:
            return idx

        
        if nums[idx] < target:
            return idx+1 
        
        else:
            return idx
        
        
        
        
