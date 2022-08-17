# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        s0 = 1
        s = n
        
        while s0 < s:
            mid = (s+s0)//2
            if isBadVersion(mid):
                s = mid 
            else:
                s0 = mid+1 
            
        return s0