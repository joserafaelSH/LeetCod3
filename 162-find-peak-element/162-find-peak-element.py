class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
    
        if len(nums) == 1:
            return 0 
        
        s0 = 0
        s = len(nums)-1
        
        while s0 < s:
            mid = (s+s0)//2
            
#             if mid == len(nums)-1:
#                 if nums[mid] > nums[mid-1] :
#                     return mid
            
#             if mid == 0:
#                 if nums[mid] > nums[mid+1] :
#                     return mid
            
#             if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
#                 return mid

            if nums[mid] < nums[mid+1]:
               
                s0 = mid+1 
            else:
                 s = mid

        return s0