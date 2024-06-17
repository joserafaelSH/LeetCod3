class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = len(nums1) - 1
        for j in nums2:
            nums1[i] = j
            i-=1 
        
        nums1.sort()
        
   



        