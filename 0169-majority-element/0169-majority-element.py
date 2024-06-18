class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        freq = {}
        n = (len(nums)//2) + 1

        resp = 0
        for v in nums:
            if v in freq:
                freq[v] +=1
                if freq[v] >= n:
                    return v
            else:
                freq[v] = 1

        return resp
            
        
