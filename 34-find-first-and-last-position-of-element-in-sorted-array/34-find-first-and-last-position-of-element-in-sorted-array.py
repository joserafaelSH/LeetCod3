class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        #busca binaria  do numero
        # se achou, add index
        # se nao achou return [-1, -1]
        
        res = []
        
        
        def bs(nums:List[int], target:int) -> int:
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
        
        r  = bs(nums,target)
        print(r)
        
        if r == -1 :
            return [-1,-1]
        else:
            res.append(r)
            for i in range(r+1, len(nums)):
                if nums[i] == target:
                    res.append(i)
            
            for i in range(r-1, -1, -1):
                if nums[i] == target:
                    res.append(i)
            
            
            if len(res) == 1:
                return [res[0], res[0]]
            else:
                res.sort()
                return [res[0], res[-1]]
        
            
            