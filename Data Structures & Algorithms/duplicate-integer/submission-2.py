class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        keys = []
        for i in range(len(nums)):
            if nums[i] in keys:
                return True
            else:
                keys.append(nums[i])
        
        return False