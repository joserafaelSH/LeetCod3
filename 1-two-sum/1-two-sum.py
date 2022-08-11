class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        sol = []
        for i in range(len(nums)):
            aux = target - nums[i]
            if aux in hash:
                sol.append(nums.index(hash.get(aux)))
                sol.append(i)
                return sol
            hash[nums[i]] = nums[i]

        return sol