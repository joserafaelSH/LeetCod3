class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
       
        size_nums1 = m - 1 
        size_nums2 = n - 1
        w = m + n - 1 
     
        while size_nums2 >=0:
            if size_nums1 >= 0 and nums1[size_nums1] >  nums2[size_nums2] :
                nums1[w] = nums1[size_nums1]
                
                size_nums1-=1
            else:
                nums1[w] = nums2[size_nums2]
                size_nums2-=1
            
            w-=1 
            
         


        